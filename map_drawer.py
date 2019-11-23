import folium
import geopandas as gpd
import pandas as pd

from flask import Flask
from shapely.geometry import *

app = Flask(__name__)

# Loading GeoJson with MSK districts into gdf.
fr = "mo.geojson"
gdf = gpd.read_file(fr)
pdf = pd.read_json("photo_coordinates.json", orient="records")
rdf = gpd.GeoDataFrame(pdf, geometry=gpd.points_from_xy(pdf.long, pdf.lat))

poly_data = {}

for _, row in rdf.iterrows():
    point: Point = row["geometry"]
    for _, r2 in gdf.iterrows():
        if point.within(r2.geometry):
            if poly_data.get(r2.NAME):
                if poly_data[r2.NAME][1]:
                    poly_data[r2.NAME][1] += 1
            else:
                poly_data[r2.NAME] = []
                poly_data[r2.NAME].append(r2.NAME)
                poly_data[r2.NAME].append(1)
            break


poly_data = pd.DataFrame.from_dict(poly_data, orient="index", columns=["district", "num"])

# Convert the GeoDataFrame to WGS84 coordinates
map_data = folium.features.Choropleth(geo_data=gdf, data=poly_data, columns=["district", "num"],
                                      key_on="feature.properties.NAME",
                                      fill_color='YlOrRd',
                                      fill_opacity=0.6,
                                      legend_name='Кол-во результатов по запросу (точек): ')

# Initializing Folium map
mmap = folium.Map((55.75, 37.61), zoom_start=10)

mmap.add_child(map_data)


@app.route("/")
def index():
    return mmap._repr_html_()


if __name__ == '__main__':
    app.run()
