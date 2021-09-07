# Simplifier

Python console script for simplifying polygons

## installation

```bash
python -m venv ./.env
. ./.env/bin/activate
# for Windows user
. ./.env/Scripts/activate
pip install -r ./requirements.txt

python -m simplifier -p .\example_data\lvl6.zip -s 0.01
```

For Windows user:

- Go to [Unofficial Windows Binaries for Python Extension Packages](https://www.lfd.uci.edu/~gohlke/pythonlibs/).
- Download on a specific folder the following binaries: GDAL, Pyproj, Fiona, Shapely and Geopandas matching the version of Python, and whether the 32-bit or 64-bit OS is installed on your laptop.
- installation using pip.

    ```bash
    pip install .\GDAL-3.1.1-cp37-cp37m-win_amd64.whl
    pip install .\pyproj-2.6.1.post1-cp37-cp37m-win_amd64.whl
    pip install .\Fiona-1.8.13-cp37-cp37m-win_amd64.whl
    pip install .\Shapely-1.7.0-cp37-cp37m-win_amd64.whl
    pip install .\geopandas-0.8.0-py3-none-any
    ```
