import folium as f
import streamlit as st
folium_map = f.Map([33.8994,35.51775], zoom_start=14)

landcover = "https://raw.githubusercontent.com/sintayehua/cmw_streamlit/main/data/landcover.tif"

raster_layer = f.raster_layers.TileLayer(tiles = landcover)
raster_layer.add_to(folium_map)

html_map = folium_map._repr_html_()
st.markdown(html_map, unsafe_allow_html =True)
