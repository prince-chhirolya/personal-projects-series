# Write Task 11 code here
import streamlit as st
import plotly.express as px
import pydeck as pdk

# FIG 1
def run(df):
    st.subheader("Plot # 01:")
    fig1 = px.scatter_3d(df, 
           x = 'passenger_count', 
           y = 'distance', 
           z = 'duration',
           color = 'passenger_count', 
           title = "3D Scatter plot",
           width = 800, 
           height = 600)
    st.plotly_chart(fig1)

# Write Task 12 code here
    st.subheader("Plot # 02:")

    df = df.explode(['polyline_lat', 'polyline_lon'], ignore_index=True)

    # Initialize components of pydeck graph
    view = pdk.data_utils.compute_view(df[["polyline_lon", "polyline_lat"]])
    view.pitch = 75
    view.bearing = 60
    view.latitude = df['polyline_lat'].iloc[-1]
    view.longitude = df['polyline_lon'].iloc[-1]
    view.zoom = 8
    view.min_zoom = 3
    view.max_zoom = 30

    layer = pdk.Layer(
          'HexagonLayer',
           df,
           get_position = ['polyline_lon', 'polyline_lat'],
           auto_highlight = True,
           elevation_scale = 50,
           get_radius = 5,
           pickable = True, # This allows a point to be picked for the tooltip.
           extruded = True, # This allows elevation
           elevation_range = [0, 3000],
           coverage = 1,
           getTextAnchor = '"middle"',
           get_alignment_baseline = '"bottom"')

    tooltip = {
           "html": 
           "No. of Rides taken from here: {elevationValue}"
            }

    # Create pld.Deck Object
    r = pdk.Deck(
        layers = [layer],
        initial_view_state = view,
        tooltip = tooltip
        )

    # Display in app
    st.pydeck_chart(r)