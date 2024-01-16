import subprocess

# infos about docker versions: https://github.com/OSGeo/gdal/tree/master/docker
# ref and thx: https://gis.stackexchange.com/a/420916/49900 
# docker run --rm -v /home/user/data:/data osgeo/gdal:ubuntu-full-3.4.1 ogr2ogr -f GeoJSON /data/myShapefile.geojson /data/myShapefile.shp

IMG = "ghcr.io/osgeo/gdal:alpine-normal-latest"

runstring = f'docker run --rm -v /data:/data {IMG} ogr2ogr -f GeoJSON /data/myShapefile.geojson /data/myShapefile.shp'
