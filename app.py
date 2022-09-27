import streamlit as st
from subprocess import call
from pathlib import Path
import pandas as pd
import plotly.express as px


def install_packages():
    call(['pip','install','TikTokApi'])
    call(['playwright','install'])
    call(['pip','install','pandas'])


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
            width: 60%;
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
st.sidebar.markdown("Here's how it works : <br>1. Enter <i>hashtag</i> you wish to analyze <br> 2. Hit <i>Get Data</i> <br>3. Analyze data with charts ",unsafe_allow_html=True)


#input
#hashtag1=st.text_input('Search hashtags . . .',value="0")

#if st.button('Get Data 1'):
#    st.write(hashtag1)
#    call(hashtag1.split(' '))

#Title
st.title("Tiktok Data Analysis")

hashtag=st.text_input('Search hashtags . . .',value="1")

#Button
if st.button('Get Data'):
    st.write(hashtag)
    
    #Check if packages are installed, if not then install them
    f=open('packages_installed.txt','r')
    pac_installed=f.read()
    f.close()
    if pac_installed==str(0):
        install_packages()
        f=open('packages_installed.txt','w')
        f.write('1')
        f.close()
        
    
    #Running tiktok.py file to get data of givn hashtag
    call(['python','tiktok.py',hashtag])
    
    #Load data from 'processed_tiktok.csv' file
    df=pd.read_csv('processed_tiktok.csv')
    
    #Changing bool columns to string because on website bool columns appears as checkbox
    bool_cols=[col for col in df.columns if df[col].dtype == 'bool']
    df[bool_cols]=df[bool_cols].astype('str') 
    
    #Plotting bar graph
    hist_df=pd.DataFrame()
    hist_df['username']=df.author_uniqueId
    hist_df['likes']=df.stats_diggCount
    hist_df['description']=df.desc
    
    
    fig=px.bar(hist_df,x='description',y='likes',hover_data=['username'] )
    fig.update_layout( xaxis_title="Description",yaxis_title="Likes" )
    st.plotly_chart(fig,use_container_width=True)
    
    del hist_df
    
    #header
    st.header("Top posts based on :")


    top_3_df=pd.DataFrame()
    top_3_df['tiktok_engagement_rate']=round( ( df.stats_diggCount + df.stats_commentCount + df.stats_shareCount ) / df.stats_playCount *100 ,3)
    top_3_df['Likes']= df.stats_diggCount 
    top_3_df['Views']= df.stats_playCount 
    top_3_df['username']=df.author_uniqueId
    top_3_df['video_id']=df.video_id
    
    #Tabs
    tabs_name=["Engagement Rate", "Likes", "Views"]
    tabs=st.tabs(tabs_name)
    
    for tab_index,tab in enumerate(tabs):
        with tab:
           
            if tab_index==0:
                top_3=top_3_df.sort_values(by='tiktok_engagement_rate',ascending=False).reset_index(drop=True).iloc[:3]
                y_axis_label='tiktok_engagement_rate'
            elif tab_index==1:
                top_3=top_3_df.sort_values(by='Likes',ascending=False).reset_index(drop=True).iloc[:3]
                y_axis_label='Likes'
            else:
                top_3=top_3_df.sort_values(by='Views',ascending=False).reset_index(drop=True).iloc[:3]
                y_axis_label='Views'
                

            #show in site
            #top_3
            
            #Plot bar graph
            fig=px.bar(top_3,x='username',y=y_axis_label,hover_data=['username'] )
            
            if tab_index==0:
                fig.update_layout( xaxis_title='Username (@)',yaxis_title=tabs_name[tab_index]+" (%)" )
            else:
                fig.update_layout( xaxis_title='Username (@)',yaxis_title=tabs_name[tab_index] )
                
            st.plotly_chart(fig,use_container_width=True)
            
            
            #Columns
            cols=st.columns(3) 
        
            for i,col in enumerate(cols):
                col.header( (df['author_nickname'][df['video_id']==top_3.loc[i,'video_id']]).values[0]  )
                col.write("username (@) : {}".format( (df['author_uniqueId'][df['video_id']==top_3.loc[i,'video_id']]).values[0] ))
                col.write("Video description : {}".format( (df['desc'][df['video_id']==top_3.loc[i,'video_id']]).values[0] ))
                col.write("Followers : {}".format( (df['authorStats_followerCount'][df['video_id']==top_3.loc[i,'video_id']]).values[0] )) 
                col.write("Engagement rate : {} %".format( top_3.loc[i,'tiktok_engagement_rate'] ) )
                col.write("Views : {}".format( (df['stats_playCount'][df['video_id']==top_3.loc[i,'video_id']]).values[0] )) 
                col.write("Likes : {}".format( (df['stats_diggCount'][df['video_id']==top_3.loc[i,'video_id']]).values[0] ))
                col.write("Comments : {}".format( (df['stats_commentCount'][df['video_id']==top_3.loc[i,'video_id']]).values[0] ))
                col.write("Shares : {}".format( (df['stats_shareCount'][df['video_id']==top_3.loc[i,'video_id']]).values[0] ))
                col.write("Video ID : {}".format( (df['video_id'][df['video_id']==top_3.loc[i,'video_id']]).values[0] ))
            
        
    #Split Columns
    left_col,right_col=st.columns(2)
    
    #Left chart header
    left_col.header("")
    left_col.header("Video Stats")
    
    #Left chart : Video stats
    video=pd.DataFrame()
    video['Views']=df.stats_playCount
    video['Comments']=df.stats_commentCount
    video['Likes']=df.stats_diggCount
    video['username']=df.author_uniqueId
    video['video_id']=df.video_id
    
    
    scatter1=px.scatter(video,x='Comments',y='Likes',hover_data=['username','video_id'],size='Views',color='Views')
    #scatter1.update_layout( xaxis_title="Shares",yaxis_title="Comments" )
    left_col.plotly_chart(scatter1,use_container_width=True)
    
    del video
    
    #Right chart header
    right_col.header("")
    right_col.header("User Stats")
    
    #Left chart : Video stats
    author=pd.DataFrame()
    author['Followers']=df.authorStats_followerCount
    author['Videos']=df.authorStats_videoCount
    author['Likes']=df.authorStats_heartCount
    author['username']=df.author_uniqueId
    
    scatter2=px.scatter(author,x='Videos',y='Followers',hover_data=['username'],size='Likes',color='Likes')
    #scatter2.update_layout( xaxis_title="Views",yaxis_title="Likes" )
    right_col.plotly_chart(scatter2,use_container_width=True)
    
    del author
    
    #Show tabular data
    st.header("Processed Data")
    df

st.write("Github Repository : [https://github.com/pushpakgote/tiktok_data_analysis](https://github.com/pushpakgote/tiktok_data_analysis)")