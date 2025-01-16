import folium as f
import streamlit as st
from streamlit_folium import folium_static

# Create a Folium map centered at a specific location
folium_map = f.Map([12, 36], zoom_start=14)

# URL to the raster file
landcover = "https://raw.githubusercontent.com/sintayehua/cmw_streamlit/main/data/landcover.tif"

# Define the bounds of the raster image
bounds = [[33.895, 35.510], [33.905, 35.525]]

# Add the raster layer to the Folium map
raster_layer = f.raster_layers.ImageOverlay(image=landcover, bounds=bounds)
raster_layer.add_to(folium_map)

# Display the map in Streamlit
folium_static(folium_map)
