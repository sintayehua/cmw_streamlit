import folium as f
import streamlit as st
import rasterio
from streamlit_folium import folium_static

# URL to the raster file
landcover = "https://raw.githubusercontent.com/sintayehua/cmw_streamlit/main/data/landcover.tif"
raster = rasterio.open(landcover)
bounds = raster.bounds
center = [(bounds.top + bounds.bottom) / 2, (bounds.left + bounds.right) / 2]

# Create a Folium map centered at a specific location
folium_map = f.Map(location=center, zoom_start=10)


# Define the bounds of the raster image
#bounds = [[9.748, 11.354], [36.868, 38.656]]

# Add the raster layer to the Folium map
raster_layer = f.raster_layers.ImageOverlay(image=raster, bounds=bounds)
raster_layer.add_to(folium_map)

# Display the map in Streamlit
folium_static(folium_map)
