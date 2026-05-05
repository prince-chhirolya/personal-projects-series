import streamlit as st
import pandas as pd
import numpy as np
import polyline
import googlemaps
from googlemaps import convert


def run(df):
    
    f = open("api_key.txt", "r")
    api_key= f.readline();
    client = googlemaps.Client(api_key)


    # Display the dataframe
    # Actual dataset had some discrepancy with column "trip_time_in_secs", 
    # so we have named it "trip_time_in_mins"
    st.subheader("Initial Dataset:")
    st.dataframe(df)


    #Rename the columns and remove any unnecessary characters from column names
    df.rename(columns = {'medallion':'ID'}, inplace = True)
    df.columns = df.columns.str.replace('[#,@,&, ]', '')    
    df.drop(columns=[ 'hack_license', 'vendor_id', 'rate_code', 'store_and_fwd_flag', 'trip_time_in_mins', 'trip_distance'], axis=1, inplace=True)
    
    # Drop useless columns
    df['duration']=0
    df['distance']=0
    df['polyline']=np.empty((len(df), 0)).tolist()
    df['polyline_lat']=np.empty((len(df), 0)).tolist()
    df['polyline_lon']=np.empty((len(df), 0)).tolist()
    
    # Display the dataframe
    st.subheader("Cleaned Dataset:")
    st.dataframe(df)




    # Finds polyline of each trip
    """Performs requests to the Google Maps Directions API."""

    def directions(client, origin, destination,
                mode=None, waypoints=None, alternatives=False, avoid=None,
                language=None, units=None, region=None, departure_time=None,
                arrival_time=None, optimize_waypoints=False, transit_mode=None,
                transit_routing_preference=None, traffic_model=None):
    

        params = {
            "origin": convert.latlng(origin),
            "destination": convert.latlng(destination)
        }

        if mode:
            # NOTE(broady): the mode parameter is not validated by the Maps API
            # server. Check here to prevent silent failures.
            if mode not in ["driving", "walking", "bicycling", "transit"]:
                raise ValueError("Invalid travel mode.")
            params["mode"] = mode

        if waypoints:
            waypoints = convert.location_list(waypoints)
            if optimize_waypoints:
                waypoints = "optimize:true|" + waypoints
            params["waypoints"] = waypoints

        if alternatives:
            params["alternatives"] = "true"

        if avoid:
            params["avoid"] = convert.join_list("|", avoid)

        if language:
            params["language"] = language

        if units:
            params["units"] = units

        if region:
            params["region"] = region

        if departure_time:
            params["departure_time"] = convert.time(departure_time)

        if arrival_time:
            params["arrival_time"] = convert.time(arrival_time)

        if departure_time and arrival_time:
            raise ValueError("Should not specify both departure_time and"
                            "arrival_time.")

        if transit_mode:
            params["transit_mode"] = convert.join_list("|", transit_mode)

        if transit_routing_preference:
            params["transit_routing_preference"] = transit_routing_preference

        if traffic_model:
            params["traffic_model"] = traffic_model

        return client._request("/maps/api/directions/json", params).get("routes", [])





    # Since API call is expensive, Here we are taking only 20 trips. This number can be changed as per requirement
    n=20
    for x in range(n):
        origin=str(df['pickup_latitude'][x]) + ',' + str(df['pickup_longitude'][x])
        destination=str(df['dropoff_latitude'][x]) + ',' + str(df['dropoff_longitude'][x])
        api_response=directions (client, origin, destination)
        miles= ( api_response[0]['legs'][0]['distance']['text'] ).split(' ', 1)[0]
        mins= ( api_response[0]['legs'][0]['duration']['text'] ).split(' ', 1)[0]
        polyline_points=(api_response[0]['overview_polyline']['points'] )
        df['duration'][x]=mins
        df['distance'][x]=miles
        df['polyline'][x]= (polyline.decode(polyline_points))
    df=df.to_csv('mydataset.csv',index=False)

def lat_lon_conversion(dataFile):
    # Do some more processing. This function takes a lat-long list and separates lat and Lon of each trip
    df=pd.read_csv(dataFile)
    n=20
    df = df.head(n)

    # Convert string to list
    df['polyline'] = df['polyline'].apply(eval)

    count=0
    # Now tuples are being identified and iterated well
    for i in (df['polyline']):
        list_lat=[]
        list_lon=[]

        # i is list
        for x in i:
            # x is a tuple, x[0] and x[1] are elements
            list_lat.append(x[0])
            list_lon.append(x[1])
        df['polyline_lat'][count]=list_lat
        df['polyline_lon'][count]=list_lon
        count=count+1
    
    # Display the dataframe
    st.subheader("Dataset Prepared for the Application:")
    return df

    