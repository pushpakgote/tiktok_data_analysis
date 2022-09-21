from TikTokApi import TikTokApi as tiktok
import json
import streamlit as st

#Get cookie data
verifyFp=""

#Setup Instance
#api = tiktok(executable_path="/path/to/chromedriver",custom_verify_fp=verifyFp,use_test_endpoints=True)

#get data by hashtags
#trending=api.hashtags('python')
#print(trending)



#with tiktok() as api:
#    for trending_video in api.trending.videos(count=50):
#        # Prints the author's username of the trending video.
#        print(trending_video.author.username)
        

if st.button('Get Data'):
    with tiktok() as api:
        for trending_video in api.trending.videos(count=50):
            # Prints the author's username of the trending video.
            print(trending_video.author.username)
        
