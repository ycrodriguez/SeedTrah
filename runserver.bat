@echo off
color 0A
echo Iniciando servidor de Django...
echo Presiona Ctrl+C para detener el servidor.
call venv\Scripts\activate.bat
python manage.py runserver
pause >nul
taskkill /f /im python.exe >nul
echo Servidor de Django detenido.