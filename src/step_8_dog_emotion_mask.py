"""Optimised real-time emotion-based animal filter. Press Q or Esc to quit."""
from collections import Counter, deque
from pathlib import Path
import sys
import cv2

from step_7_fer import get_image_to_emotion_predictor

HERE = Path(__file__).resolve().parent
ASSETS = HERE / "assets"


def apply_mask(face, mask):
    """Fit a white-background mask into a face region without changing its size."""
    if face is None or face.size == 0 or mask is None:
        return face
    fh, fw = face.shape[:2]
    mh, mw = mask.shape[:2]
    if min(fh, fw, mh, mw) <= 0:
        return face
    scale = min(fh / mh, fw / mw)
    nw, nh = max(1, int(mw * scale)), max(1, int(mh * scale))
    resized = cv2.resize(mask, (nw, nh), interpolation=cv2.INTER_AREA)
    result = face.copy()
    ox, oy = (fw - nw) // 2, (fh - nh) // 2
    roi = result[oy:oy + nh, ox:ox + nw]
    # The supplied PNG masks use white as transparent background.
    visible = (resized < 245).any(axis=2)
    roi[visible] = resized[visible]
    return result


def open_camera():
    """Try Windows DirectShow first, then OpenCV's default backend."""
    if sys.platform == "win32":
        camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        if camera.isOpened():
            return camera
        camera.release()
    return cv2.VideoCapture(0)


def main():
    camera = open_camera()
    if not camera.isOpened():
        print("ERROR: Could not open webcam. Close other camera apps and check Windows camera permissions.")
        return

    # A smaller frame reduces the work needed for face detection.
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    camera.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    mask_files = ["dog.png", "dalmation.png", "sheepdog.png"]
    masks = [cv2.imread(str(ASSETS / name)) for name in mask_files]
    if any(mask is None for mask in masks):
        missing = [name for name, mask in zip(mask_files, masks) if mask is None]
        print("ERROR: Missing/unreadable mask image(s):", ", ".join(missing))
        camera.release()
        return

    cascade = cv2.CascadeClassifier(str(ASSETS / "haarcascade_frontalface_default.xml"))
    if cascade.empty():
        print("ERROR: Could not load the face-detection XML file in src/assets.")
        camera.release()
        return

    model_path = ASSETS / "model_best.pth"
    if not model_path.exists():
        print("ERROR: Model file not found:", model_path)
        camera.release()
        return

    print("Loading emotion model... please wait.")
    try:
        predictor = get_image_to_emotion_predictor(str(model_path))
    except Exception as exc:
        print("ERROR while loading emotion model:", exc)
        camera.release()
        return

    print("Filter is running. Press Q or Esc in the camera window to quit.")
    frame_number = 0
    face_box = None
    previous_box = None
    missed_detections = 0
    emotion_votes = deque(maxlen=7)
    emotion_index = 0
    detect_every = 3
    predict_every = 9
    smoothing = 0.65

    try:
        while True:
            ok, frame = camera.read()
            if not ok or frame is None:
                print("Camera stopped returning frames. Check that it is not being used by another app.")
                break

            frame_number += 1
            frame = cv2.flip(frame, 1)
            height, width = frame.shape[:2]

            if frame_number % detect_every == 0:
                # Detect on a half-size frame to reduce CPU load.
                small = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
                gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
                gray = cv2.equalizeHist(gray)
                faces = cascade.detectMultiScale(
                    gray, scaleFactor=1.15, minNeighbors=5,
                    minSize=(35, 35), flags=cv2.CASCADE_SCALE_IMAGE
                )
                if len(faces):
                    x, y, w, h = max(faces, key=lambda box: box[2] * box[3])
                    detected = (int(x * 2), int(y * 2), int(w * 2), int(h * 2))
                    if previous_box is None:
                        face_box = detected
                    else:
                        face_box = tuple(
                            int(smoothing * old + (1 - smoothing) * new)
                            for old, new in zip(previous_box, detected)
                        )
                    previous_box = face_box
                    missed_detections = 0
                else:
                    missed_detections += 1
                    # Briefly retain the last box to prevent one missed frame
                    # from making the overlay flash off and on.
                    if missed_detections > 5:
                        face_box = None
                        previous_box = None
                        emotion_votes.clear()

            if face_box is not None:
                x, y, w, h = face_box
                x0 = max(0, x)
                y0 = max(0, y - int(0.25 * h))
                x1 = min(width, x + w)
                y1 = min(height, y + int(0.75 * h))
                fx0, fy0 = max(0, x), max(0, y)
                fx1, fy1 = min(width, x + w), min(height, y + h)

                if frame_number % predict_every == 0 and fx1 > fx0 and fy1 > fy0:
                    crop = frame[fy0:fy1, fx0:fx1]
                    try:
                        emotion_votes.append(predictor(crop))
                        emotion_index = Counter(emotion_votes).most_common(1)[0][0]
                    except Exception as exc:
                        print("Emotion prediction warning:", exc)

                if x1 > x0 and y1 > y0:
                    # The model has exactly three output classes.
                    emotion_index = max(0, min(2, int(emotion_index)))
                    frame[y0:y1, x0:x1] = apply_mask(
                        frame[y0:y1, x0:x1], masks[emotion_index]
                    )

            cv2.imshow("Emotion-Based Dog Filter | Q to quit", frame)
            key = cv2.waitKey(1) & 0xFF
            if key in (ord('q'), 27):
                break
    finally:
        camera.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
