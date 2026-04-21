@echo off
REM === Go to project folder ===
cd /d "E:\project\Malayalam_Cloner"

REM === Activate virtualenv (edit this path if your venv name is different) ===
call E:\project\Malayalam_Cloner\venv\Scripts\activate

REM === Run the app ===
python app.py

REM Optional: keep window open after exit
pause
