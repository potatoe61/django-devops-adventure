call C:\api\.venv\Scripts\activate.bat
pause
waitress-serve --listen=127.0.0.1:8001 testapi.wsgi:application
pause
cmd /k