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
        m.split_map(
            left_layer=landcover, left_args={"colormap_name": "terrain", "nodata": 0}, 
            right_layer=landcover
        )
        #m.add_legend(title="ESA Land Cover", builtin_legend="ESA_WorldCover")
        #m.add_raster(landcover, colormap="terrain", layer_name="Landcover")
        #m.add_legend()
        #m.split_map(
        #    left_layer="ESA WorldCover 2020 S2 FCC", right_layer="ESA WorldCover 2020"
        #)
        #m.add_legend(title="ESA Land Cover", builtin_legend="ESA_WorldCover")
    
m.to_streamlit(height=700)
