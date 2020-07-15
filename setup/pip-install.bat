REM Use the packed conda environment to pip install arguments
REM (makes sure the environment is set up properly before doing so)

REM set up environment variables
SET PATH=%~dp0Dependencies\Python;%~dp0Dependencies\Python\Scripts;%PATH%
SET PATH=%~dp0Dependencies\Python\Library\bin;%~dp0Dependencies\Daysim;%PATH%
SET PYTHONHOME=%~dp0Dependencies\Python
SET GDAL_DATA=%~dp0Dependencies\Python\Library\share\gdal
SET PROJ_LIB=%~dp0Dependencies\Python\Library\share
SET RAYPATH=%~dp0Dependencies\Daysim

REM call pip...
CALL %~dp0Dependencies\Python\python.exe -m pip install %*