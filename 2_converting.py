import subprocess
import os
from time import sleep,time

ogr2ogr_path = r"C:\OSGeo4W\bin\ogr2ogr.exe"
filename = 'osm_data.parquet'

# ogr2ogr -f MVT  "C:\Users\kaue\Documents\tiles" "C:\Users\kaue\Documents\other_footways.parquet" -dsco MAXZOOM=22

runstring_foldertiles = f'{ogr2ogr_path} -f MVT tiles "{filename}" -dsco MAXZOOM=22 -progress'
runstring_mbtiles = f'{ogr2ogr_path} -f MVT tiles "{filename}.mbtiles" -dsco MAXZOOM=22 -progress'
runstring_pmtiles = f'{ogr2ogr_path} -f PMTiles tiles "{filename}.pmtiles" -dsco MAXZOOM=22 -progress'

for runstring in [runstring_foldertiles, runstring_mbtiles, runstring_pmtiles]:
    t1 = time()
    subprocess.run(runstring, shell=True)
    print(f'took {time()-t1} seconds')