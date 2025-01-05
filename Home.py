import streamlit as st
import leafmap.leafmap as leafmap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://raw.githubusercontent.com/sintayehua/cmw_streamlit/main/data/dmu.png"
st.sidebar.image(logo)

# Customize page title
st.title("Choke Mountain Watersheds (CMW)")

st.markdown(
    """
    A streamlit web app to showcase geospatial datasets produced for the CMW
    """
)

st.header("Background")

markdown = """
The Choke Mountain watersheds, located in the Amhara Region of Ethiopia, are a vital ecological zone characterized by their rich biodiversity and significant water resources. These watersheds play a crucial role in supporting local agriculture, providing water for irrigation, and sustaining various forms of wildlife. The region is known for its unique highland ecosystems, which include a variety of endemic plant and animal species. Additionally, the Choke Mountain watersheds contribute to the livelihoods of the surrounding communities by offering resources for farming, fishing, and other economic activities.

"""

st.markdown(markdown)

m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)
