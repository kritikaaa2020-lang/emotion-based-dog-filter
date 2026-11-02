EMOTION-BASED DOG FILTER - OPENING GUIDE (WINDOWS + VS CODE)
============================================================

IMPORTANT: Keep the complete extracted project folder together. Do not move
individual Python files out of src or remove the src/assets folder. The trained
model, face-detection XML, and animal masks are required.

FIRST TIME ONLY
---------------
1. Extract this ZIP file (right-click it > Extract All...).
2. Open VS Code.
3. Choose File > Open Folder.
4. Select the extracted folder named emotion-based-dog-filter-master.
5. Install Python 3.12 (64-bit) if it is not already installed.
6. Close other apps that may be using your webcam (Camera, Zoom, Teams, etc.).
7. In VS Code, you can either double-click setup_windows.bat in File Explorer,
   or open Terminal > New Terminal and run:
       .\setup_windows.bat
8. Wait for installation to finish. It needs an internet connection.

EVERY TIME YOU WANT TO OPEN THE PROJECT LATER
---------------------------------------------
1. Open VS Code.
2. File > Open Folder > choose the extracted
   emotion-based-dog-filter-master folder.
3. Double-click run_filter.bat in Windows File Explorer.
   OR in the VS Code terminal, run:
       .un_filter.bat
4. Wait for the model to load. The webcam window should appear.
5. Click the webcam window and press Q (or Esc) to close it.

OPTIONAL: TEST THE WEBCAM ONLY
------------------------------
Double-click test_webcam.bat, or run:
    .	est_webcam.bat

IF YOU WANT TO RUN IT MANUALLY IN VS CODE
-----------------------------------------
Open Terminal > New Terminal, then run:
    .env\Scripts\Activate.ps1
    cd src
    python step_8_dog_emotion_mask.py

If PowerShell blocks activation, use the .bat launchers above instead.

TROUBLESHOOTING
---------------
- Webcam won't open: close other camera apps; check Windows Settings >
  Privacy & security > Camera and allow desktop apps to access the camera.
- Camera freezes: disconnect/reconnect the webcam and try again; avoid running
  two camera apps at once.
- Missing model/mask/XML: restore the original src/assets folder from this ZIP.
- Import error: run .\setup_windows.bat again from the project root.
- If a different error appears, copy the complete terminal error message.

PERFORMANCE NOTES
-----------------
This version reduces camera resolution, performs face detection every few
frames, predicts emotion less often, smooths face position and emotion votes,
and always releases the webcam on exit. Performance still depends on your
computer and webcam. The included 2017-era model is a small three-class demo;
it is not a modern Snapchat-grade face or emotion detector.

Project files and assets are based on the original project. The improved
webcam runner and setup guide are included for easier use on Windows.
