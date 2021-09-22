set mydir=%~dp0

Powershell -Command "& { Start-Process \"%mydir%setdate.bat\" -verb RunAs}"