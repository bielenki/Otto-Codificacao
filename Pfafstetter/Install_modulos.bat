@echo off
:start
REM set the python version here
set python_ver=27
set arcgis_ver=10.6
cls

echo.
echo.
echo Atualizando o PIP
echo ================
echo.
cd \
cd \python%python_ver%\Arcgis%arcgis_ver%\Scripts\
pip install --upgrade pip
pause

echo.
echo.
echo Up grade do modulo NUMPY
echo ================
echo.
cd \
cd \python%python_ver%\Arcgis%arcgis_ver%\Scripts\
pip install --upgrade numpy
pause

echo.
echo.
echo Instalando o modulo PANDAS
echo ================
echo.
cd \
cd \python%python_ver%\Arcgis%arcgis_ver%\Scripts\
pip install c:\Pfafstetter\Wheel\pandas-0.24.2-cp27-cp27m-win32.whl
pause

echo.
echo.
echo Instalando o modulo GDAL
echo ================
echo.
cd \
cd \python%python_ver%\Arcgis%arcgis_ver%\Scripts\
pip install c:\Pfafstetter\Wheel\GDAL-2.2.4-cp27-cp27m-win32.whl
pause

echo.
echo.
echo Instalando o modulo FIONA
echo ================
echo.
cd \
cd \python%python_ver%\Arcgis%arcgis_ver%\Scripts\
pip install c:\Pfafstetter\Wheel\Fiona-1.8.4-cp27-cp27m-win32.whl
pause

echo.
echo.
echo Instalando o modulo CYTHON
echo ================
echo.
cd \
cd \python%python_ver%\Arcgis%arcgis_ver%\Scripts\
pip install cython
pause

echo.
echo.
echo Instalando o modulo PYPROJ
echo ================
echo.
cd \
cd \python%python_ver%\Arcgis%arcgis_ver%\Scripts\
pip install c:\Pfafstetter\Wheel\pyproj-1.9.6-cp27-cp27m-win32.whl
pause

echo.
echo.
echo Instalando o modulo SHAPELY
echo ================
echo.
cd \
cd \python%python_ver%\Arcgis%arcgis_ver%\Scripts\
pip install c:\Pfafstetter\Wheel\Shapely-1.6.4.post1-cp27-cp27m-win32.whl
pause

echo.
echo.
echo Instalando o modulo GEOPANDAS
echo ================
echo.
cd \
cd \python%python_ver%\Arcgis%arcgis_ver%\Scripts\
pip install c:\Pfafstetter\Wheel\geopandas-0.4.1-py2.py3-none-any.whl
pause

echo.
echo.
echo Instalando o modulo PYSAL
echo ================
echo.
cd \
cd \python%python_ver%\Arcgis%arcgis_ver%\Scripts\
pip install c:\Pfafstetter\Wheel\PySAL-1.14.4.post2-py2-none-any.whl
pause

echo.
echo.
echo Instalação de módulos concluída
echo ================
echo.
pause
exit