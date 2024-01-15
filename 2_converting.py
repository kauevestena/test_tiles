import subprocess
import os
from time import sleep,time

ogr2ogr_path = r"C:\OSGeo4W\bin\ogr2ogr.exe"
filename = 'osm_data.gpkg'

# ogr2ogr -f MVT  "C:\Users\kaue\Documents\tiles" "C:\Users\kaue\Documents\other_footways.parquet" -dsco MAXZOOM=22

# regular_conversion = f'{ogr2ogr_path} -f GPKG test.gpkg {filename} -progress'
runstring_foldertiles = f'{ogr2ogr_path} -f MVT osm_data_tiles {filename} -dsco MINZOOM=12 -dsco MAXZOOM=20 -progress'
runstring_mbtiles = f'{ogr2ogr_path} -f MVT tiles osm_data_tiles.mbtiles {filename} -dsco MINZOOM=12 -dsco MAXZOOM=20 -progress'
runstring_pmtiles = f'{ogr2ogr_path} -f PMTiles tiles osm_data_tiles.pmtiles {filename} -dsco MINZOOM=12 -dsco MAXZOOM=20 -progress'

for runstring in [runstring_foldertiles,runstring_mbtiles, runstring_pmtiles]:
    t1 = time()
    subprocess.run(runstring, shell=True)
    print(f'took {time()-t1} seconds')