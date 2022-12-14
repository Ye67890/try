import streamlit as st
import pandas as pd
import altair as alt
import pydeck as pdk

DATA_URL = "https://hellobucketbucket.s3.ap-northeast-1.amazonaws.com/%E7%A6%8F_date_lat_lng.csv"

@st.cache
def load_data():
    data = pd.read_csv(DATA_URL, nrows = None)
    # lowercase = lambda x: str(x).lower()
    # data.rename(lowercase, axis = "columns", inplace = True)
#     data[DATE_TIME] = pd.to_datetime(data[DATE_TIME])
    return data

data = load_data()

st.write("""
# 第一個應用程式
嘗試創建**表格**
""", data)

st.subheader('Map of all pickups')
st.map(data, 10)

# st.subheader('Altair chart')
# c = alt.Chart(data).mark_circle().encode(
#     x='lon', y='lat', size='label', color='label', tooltip=['lon', 'lat', 'label'])
#
# st.altair_chart(c, use_container_width=True)

st.subheader("barchartMap")

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=23.9785,
        longitude=121.6,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=data,
           get_position='[lon, lat]',
           get_elevation=['label'],
           radius=200,
           elevation_scale=50,
           elevation_range=[0, 100],
           pickable=True,
           extruded=True,
        ),
#         pdk.Layer(
#             'ScatterplotLayer',
#             data=data,
#             get_position='[lon, lat]',
# #             get_elevation=['label'],
#             get_color='[200, 30, 0, 160]',
#             get_radius=200,
#         ),
    ],
))
