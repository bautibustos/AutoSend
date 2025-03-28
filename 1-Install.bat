@echo off

echo Creando entorno
python -m venv recursos

pause

echo Activacion de entorno virtual

set VENV_DIR=%~dp0Recursos
call %VENV_DIR%\Scripts\activate.bat
pause

echo Instalacion de librerias
pip install -r requerimientos.txt

echo Instalacion completada
pause