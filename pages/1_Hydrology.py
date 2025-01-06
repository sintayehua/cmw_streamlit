import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.title("CMW Hydrology")

with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map()
        boundary = "https://raw.githubusercontent.com/sintayehua/cmw_streamlit/main/data/cmw_max_boundary.geojson"
        climate = "https://raw.githubusercontent.com/sintayehua/cmw_streamlit/main/data/nma_stations.csv"
        flow = "https://raw.githubusercontent.com/sintayehua/cmw_streamlit/main/data/flow_stations.csv"
        landcover = "https://raw.githubusercontent.com/sintayehua/cmw_streamlit/main/data/landcover.tif"
        cog_landcover = "https://raw.githubusercontent.com/sintayehua/cmw_streamlit/main/data/landcover_cog.tif"
        m.add_geojson(boundary, layer_name="CMW boundary")
        m.add_points_from_xy(
            climate,
            x="long",
            y="lat",
            #color_column="station_name",
            #icon_names=["gear", "map", "leaf", "globe"],
            spin=True,
            add_legend=True,
        )
        m.add_points_from_xy(
            flow,
            x="lon",
            y="lat",
            #color_column="station_name",
            #icon_names=["gear", "map", "leaf", "globe"],
            spin=False,
            add_legend=True,
        )
        # Add a Legend
        colors = ['#006400', '#ffbb22','#ffff4c','#f096ff',
                  '#fa0000', '#b4b4b4','#f0f0f0','#0064c8']
        labels = ["Trees","Shrubland","Grassland","Cropland",
                  "Herbaceous wetland", "Bareland", "Built-up", "Open water"]
        colormap = {
            "1": "#006400",
            "2": "#ffbb22",
            "3": "#ffff4c",
            "4": "f096ff",
            "5": "#fa0000",
            "7": "#b4b4b4",
            "8": "#f0f0f0",
            "10": "#0064c8"}
        
        #m.add_cog_layer(cog_landcover, colormap=colormap, name="Landcover")
        m.add_raster(landcover, layer_name="Landcover")
        #m.add_legend(colors=colors, labels=labels)
        #m.add_legend(title="ESA Land Cover", builtin_legend="ESA_WorldCover")
        #m.add_raster(landcover, colormap="terrain", layer_name="Landcover")
        #m.add_legend()
        #m.split_map(
        #    left_layer="ESA WorldCover 2020 S2 FCC", right_layer="ESA WorldCover 2020"
        #)
        #m.add_legend(title="ESA Land Cover", builtin_legend="ESA_WorldCover")
    
m.to_streamlit(height=700)
