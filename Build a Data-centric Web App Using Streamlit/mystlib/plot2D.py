import streamlit as st
import plotly.express as px

def run(df, page):
    if page == '2D Charts and Histograms':
        # Plot #01: Mean Travel Time vs Passenger Count
        st.subheader("Plot # 01:")
        fig1 = px.bar(
            df.groupby('passenger_count', as_index=False)['duration'].mean(),
            x='passenger_count',
            y='duration',
            title="Mean Travel Time for No. of Passengers"
        )
        st.plotly_chart(fig1, use_container_width=True)

        # Plot #02: Distance vs Duration Scatter
        st.subheader("Plot # 02:")
        fig2 = px.scatter(
            df,
            x='duration',
            y='distance',
            color='passenger_count',
            title="Distance to Duration Relationship"
        )
        st.plotly_chart(fig2, use_container_width=True)
