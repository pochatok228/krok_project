import folium
import geopandas as gpd
import pandas as pd

from pandas.io.json import json_normalize
from flask import Flask

app = Flask(__name__)

# Loading GeoJson with MSK districts into gdf.
fr = "mo.geojson"
gdf = gpd.read_file(fr)
pdf = pd.read_json("photo_coordinates.json", orient="records")
rdf = gpd.GeoDataFrame(pdf, geometry=gpd.points_from_xy(pdf.long, pdf.lat))

# Initializing Choropleth
map_data = folium.features.Choropleth(geo_data=gdf, )

# Initializing Folium map
mmap = folium.Map((55.75, 37.61), zoom_start=10)

mmap.add_child(map_data)


@app.route("/")
def index():
    return mmap._repr_html_()


if __name__ == '__main__':
    app.run()
