import streamlit as st
from subprocess import call
from pathlib import Path
import pandas as pd
import plotly.express as px

#download
#st.download_button(
#    label="Download JSON",
#    file_name="data.json",
#    mime="application/json",
#    data=Path("tiktok_json.json").read_text(),
#)

#set page layout to wide
st.set_page_config(layout='wide')

#Sidebar

st.markdown(
    """
    <style>
        [data-testid=stSidebar] [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 50%;
        }
        [data-testid=stSidebar]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True
)

with st.sidebar:
    st.image("tiktok.png")

#st.sidebar.markdown(" <div> < img src='https://assets.stickpng.com/images/5cb78671a7c7755bf004c14b.png' width=100 /> <h1 style='display:inline-block'>TikTok Analytics</h1></div> ",unsafe_allow_html=True)
st.sidebar.markdown("<div> <h1 style='display:inline-block;text-align:center;'>TikTok Analytics</h1> </div> ",unsafe_allow_html=True)
st.sidebar.markdown("This dashboard allows you to analyze latest tiktok videos using Python and Streamlit")
#st.sidebar.markdown("Here's how it works : <ol><li>1. Enter <i>hashtag></i> you wish to analyze</li><li>2. Hit <i>Get Data</i> </li> <li>3. Analyze data with charts </li>",unsafe_allow_html=True)
st.sidebar.markdown("Here's how it works ",unsafe_allow_html=True)
st.sidebar.markdown("1. Enter <i>hashtag></i> you wish to analyze",unsafe_allow_html=True)
st.sidebar.markdown("2. Hit <i>Get Data</i> ",unsafe_allow_html=True)
st.sidebar.markdown("3. Analyze data with charts",unsafe_allow_html=True)


#input
hashtag1=st.text_input('Search hashtags . . .',value="0")

if st.button('Get Data 1'):
    st.write(hashtag1)
    call(hashtag1.split(' '))
    #call(['python','tiktok.py',hashtag])
    #with open('test.txt') as f:
    #    contents = f.read()
    #st.write(contents)
    
hashtag=st.text_input('Search hashtags . . .',value="1")

#Button
if st.button('Get Data'):
    st.write(hashtag)
    
    #Running tiktok.py file to get data of givn hashtag
    call(['python','tiktok.py',hashtag])
    
    #Load data from 'processed_tiktok.csv' file
    df=pd.read_csv('processed_tiktok.csv')
    
    #Changing bool columns to string because on website bool columns appears as checkbox
    bool_cols=[col for col in df.columns if df[col].dtype == 'bool']
    df[bool_cols]=df[bool_cols].astype('str') 
    
    #Plotting histogram
    fig=px.histogram(df,x='desc',y='authorStats_diggCount',hover_data=['desc'],height=300)
    fig.update_layout( yaxis_title="Likes" )
    st.plotly_chart(fig,use_container_width=True)
    
    #Split Columns
    left_col,right_col=st.columns(2)
    
    #Left chart : Video stats
    scatter1=px.scatter(df,x='stats_shareCount',y='stats_commentCount',hover_data=['desc'],size='stats_playCount',color='stats_playCount')
    scatter1.update_layout( xaxis_title="Shares",yaxis_title="Comments" )
    left_col.plotly_chart(scatter1,use_container_width=True)
    
    #Left chart : Video stats
    scatter2=px.scatter(df,x='authorStats_videoCount',y='authorStats_heartCount',hover_data=['author_nickname'],size='authorStats_followerCount',color='authorStats_followerCount')
    scatter2.update_layout( xaxis_title="Views",yaxis_title="Likes" )
    right_col.plotly_chart(scatter2,use_container_width=True)
    
    #Show tabular data
    df

