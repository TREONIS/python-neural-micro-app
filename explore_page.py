import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

@st.cache
def load_data():
    df = pd.read_pickle("./models/df_proper_cleaned.pkl")
    return df

df = load_data()

def show_explore_page():
    width = 800
    st.title("Activities, data and insights")

    st.write(
    """
    ### Geographic distribution of our users over the world
    """
    )
    
    image = Image.open('./images/geo_density_.png')
    st.image(image, caption='',use_column_width=True)
    
    
    st.write(
    """
    ### Example training route
    """)
    image = Image.open('./images/route_run.png')
    st.image(image, caption='',use_column_width=True)
    
    st.write(
    """
    ### Heart rate history of individual user
    """)
    image = Image.open('./images/hr_history.png')
    st.image(image, caption='',use_column_width=True)
    
    
    st.write(
    """
    ### Heart rate and Altitude
    """)
    image = Image.open('./images/hr_session_detail.png')
    st.image(image, caption='',use_column_width=True)
    
