from TikTokApi import TikTokApi as tiktok
import json
import sys
import pandas as pd
from helpers import process_result


#Get cookie data
#verifyFp=""

#Setup Instance
#api = tiktok(executable_path="/path/to/chromedriver",custom_verify_fp=verifyFp,use_test_endpoints=True)


def get_data(hashtag):
    video_data=[]
    with tiktok() as api:
        tag=api.hashtag(hashtag)
        #print('Api hashtag :', tag.info_full())
        #print('Tag info : ',tag.info())
        
        #print("tag.videos : ",tag.videos()) 
        for video in tag.videos():
            #print("inside")
            #print('Video id : ',video.author)
            #print('Video dict : ',video.as_dict)
            #print(type(video.as_dict))
            video_data.append(video.as_dict)
            

    #print(len(video_data))
    
    #Processing data
    data=process_result(video_data)

    #Exporting data to csv
    data=pd.DataFrame(data)
    data.to_csv('processed_tiktok.csv',index=False)
    


if __name__ == '__main__':
    print(get_data(sys.argv[1]) )
