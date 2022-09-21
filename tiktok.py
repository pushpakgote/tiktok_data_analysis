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
        for trending_video in api.trending.videos(count=50):
            # Prints the author's username of the trending video.
            print(trending_video.author.username)
            ls.append(trending_video.author.username)
    #ls.append(hashtag)
    
    #lines = ['Readme', 'How to write text files in Python']
    with open('test.txt', 'w') as f:
        for line in ls:
            f.write(line)
            f.write('\n')
    


if __name__ == '__main__':
    print(get_data(sys.argv[1]) )
