import streamlit as st
import leafmap.foliumap as leafmap
import os

st.set_page_config(layout="wide")

st.title("CMW Hydrology")

with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map()
        m.add_basemap("HYBRID")
        boundary = "https://raw.githubusercontent.com/sintayehua/cmw_streamlit/main/data/cmw_max_boundary.geojson"
        climate = "https://raw.githubusercontent.com/sintayehua/cmw_streamlit/main/data/nma_stations.csv"
        watersheds = "https://raw.githubusercontent.com/sintayehua/cmw_streamlit/main/data/cmw_watersheds.geojson"
        rivers = "https://raw.githubusercontent.com/sintayehua/cmw_streamlit/main/data/rivers.geojson"
        
        m.add_geojson(boundary, layer_name="CMW boundary", info_mode='on_click')
        m.add_geojson(watersheds, layer_name="Watersheds", info_mode='on_click')
        m.add_geojson(rivers, layer_name="Rivers", info_mode='on_click')
        m.add_points_from_xy(
            climate,
            x="long",
            y="lat",
            layer_name="Weather Stations",
            icon_names=["gear", "map", "leaf", "globe"],
            add_legend=True,
        )
        m.split_map(
            left_layer="ESA WorldCover 2020 S2 FCC", right_layer="ESA WorldCover 2020"
        )
        m.add_legend(title="ESA Land Cover", builtin_legend="ESA_WorldCover")
        
m.to_streamlit(height=700)
