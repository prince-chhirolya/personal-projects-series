# Write Task 7 code here

import streamlit as st
import pandas as pd
import plotly.express as px

def run(df):
    # Set mapbox token to allow plotting on map
    px.set_mapbox_access_token('<Your_Token_Here>')

    # PLOT # 1
    st.subheader("Plot # 01:")
    fig_1 = px.scatter_mapbox(df, 
            lat = "pickup_latitude", 
            lon = "pickup_longitude", 
            size = "passenger_count",
            color = "passenger_count",
            center = dict( 
                     lat = float(df["pickup_latitude"][0]),
                     lon = float(df["pickup_longitude"][0]) 
                     ), 
            zoom = 10, width = 800, height = 600)
    fig_1.update_layout(title_text = 'Passengers in Taxi Trips', title_x = 0.5, title_y = 1)
    st.plotly_chart(fig_1, use_container_width = True)

# Write Task 8 code here

    # PLOT # 2
    st.subheader("Plot # 02:")
    st.write('Select an ID to view its trip route:')
    option = st.selectbox(
             ' ', df["ID"])
    trip = df[df['ID'] == option]


    # Convert elements of a list into a column using the explode function.
    trip["lat"] = trip["polyline_lat"]
    trip["lon"] = trip["polyline_lon"]
    trip = trip.explode(['lat', 'lon'], ignore_index = True)
 
    fig_2 = px.line_mapbox(
            trip, lat = "lat", lon = "lon",  zoom = 10, 
            width = 800, height = 600)
    fig_2.update_layout(title_text = 'Trip Routes',
                        title_x = 0.5, title_y = 1)
    st.plotly_chart(fig_2, use_container_width = True)
