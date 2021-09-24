@echo off
SETLOCAL
for /f %%i in (C:\Users\MFY\Documents\GitHub\Address.txt) do CALL :RunPythonFile %%i ,

call "run.bat"

EXIT /B %ERRORLEVEL%

:RunPythonFile

cd %~1
python run.py

EXIT /B 0
