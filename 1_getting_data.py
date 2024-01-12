import osmnx as ox

# getting a massive dataset:
data = ox.features_from_place('Milan',{'highway':True})

# dealing with lists in the middle of the rest of data:
for column in data.columns:
    if data[column].dtype == object:
        data[column] = data[column].astype(str)

data.to_parquet('osm_data.parquet')