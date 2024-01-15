import folium
from folium.plugins import VectorGridProtobuf
import geopandas as gpd

url = r"https://kauevestena.github.io/test_tiles/osm_data_tiles/{z}/{x}/{y}.pbf"

print(url)

data = gpd.read_parquet('osm_data.parquet')



bounds = data.total_bounds

mid_lat = (bounds[1] + bounds[3]) / 2
mid_lgt = (bounds[0] + bounds[2]) / 2

m = folium.Map(location=[mid_lat, mid_lgt], zoom_start=12, tiles='openstreetmap')

rules =  {  
}

options = {
    "vectorTileLayerStyles": {
        "osm_data_tiles": {
            "weight": 1,
            "fillColor": "#f2b648",
            "color": "#f2b648",
            "fillOpacity": 1,
            "opacity": 1
        },
    }
}

VectorGridProtobuf(url, "test_pbf",options).add_to(m)

m.save('osm_data_tiles_folder.html')