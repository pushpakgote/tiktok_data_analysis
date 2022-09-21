from TikTokApi import TikTokApi as tiktok
import json
import sys

#Get cookie data
#verifyFp=""

#Setup Instance
#api = tiktok(executable_path="/path/to/chromedriver",custom_verify_fp=verifyFp,use_test_endpoints=True)

#get data by hashtags
#trending=api.hashtags('python')
#print(trending)

def get_data(hashtag):
    ls=[]
    with tiktok() as api:
        tag=api.hashtag(hashtag)
        print('Api hashtag :', tag.info_full())
        print('Tag info : ',tag.info())
        
        print("tag.videos : ",tag.videos()) 
        for video in tag.videos():
            print("inside")
            #print('Video id : ',video.author)
            print('Video dict : ',video.as_dict)
            #first=video.as_dict
            #break
        
        print('keys : ',video.author,video.id)
        print(video.as_dict)
        
        
        #print(api)
        for trending_video in api.trending.videos(count=50):
            # Prints the author's username of the trending video.
            print('trending : ',trending_video.author.username)
            ls.append(trending_video.author.username)
        print("Over")
    #ls.append(hashtag)
    
    #lines = ['Readme', 'How to write text files in Python']
    with open('test.txt', 'w') as f:
        for line in ls:
            f.write(line)
            f.write('\n')
    


if __name__ == '__main__':
    print(get_data(sys.argv[1]) )
