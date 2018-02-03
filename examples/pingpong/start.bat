
set SERVER_ROOT=%cd%
set FAT_SERVER_PATH=%SERVER_ROOT%\fatserver
set PYTHONPATH=%FAT_SERVER_PATH%\Lib;%FAT_SERVER_PATH%;%SERVER_ROOT%\examples\pingpong

python %SERVER_ROOT%\examples\pingpong\main.py

