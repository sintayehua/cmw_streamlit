import folium as f
import streamlit as st

# Create a Folium map centered at a specific location
folium_map = f.Map([33.8994, 35.51775], zoom_start=14)

# URL to the raster file
landcover = "https://raw.githubusercontent.com/sintayehua/cmw_streamlit/main/data/landcover.tif"

# Add the raster layer to the Folium map
raster_layer = f.raster_layers.ImageOverlay(landcover)
raster_layer.add_to(folium_map)

# Convert the Folium map to HTML
html_map = folium_map._repr_html_()

# Display the map in Streamlit
st.markdown(html_map, unsafe_allow_html=True)
