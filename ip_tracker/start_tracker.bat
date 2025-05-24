@echo off
REM Start Flask app in a new window
start python app.py

REM Wait 5 seconds for server to start
timeout /t 3 /nobreak >nul

REM Open default browser at localhost:5000
start http://127.0.0.1:5000

REM Keep this window open to see logs
pause
