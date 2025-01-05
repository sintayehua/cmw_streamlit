import streamlit as st
import leafmap.leafmap as leafmap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
CMW datasets
<https://www.dmu.edu.et>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://raw.githubusercontent.com/sintayehua/cmw_streamlit/main/data/dmu.png"
st.sidebar.image(logo)

markdown2 = """
Hydraulic and Water Resources Engineering Department

© 2025 Sintayehu Adefires Abebe
"""
st.sidebar.info(markdown2)

# Customize page title
st.title("Choke Mountain Watersheds (CMW)")

st.markdown(
    """
    A web app to showcase geospatial datasets produced for the CMW
    """
)

st.header("Background")

markdown = """
The Choke Mountain watersheds, located in the Amhara Region of Ethiopia, are a vital ecological zone characterized by their rich biodiversity and significant water resources. These watersheds play a crucial role in supporting local agriculture, providing water for irrigation, and sustaining various forms of wildlife. The region is known for its unique highland ecosystems, which include a variety of endemic plant and animal species. Additionally, the Choke Mountain watersheds contribute to the livelihoods of the surrounding communities by offering resources for farming, fishing, and other economic activities.

"""

st.markdown(markdown)

photo = "https://raw.githubusercontent.com/sintayehua/cmw_streamlit/main/data/choke.jpg"
st.image(photo)

m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)
