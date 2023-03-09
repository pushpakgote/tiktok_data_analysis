'''
from TikTokApi import TikTokApi

print("inside test.py")
# Watch https://www.youtube.com/watch?v=-uCt1x8kINQ for a brief setup tutorial
with TikTokApi() as api:
    print("inside 1st loop")
    #for trending_video in api.trending.videos(count=20):
    tag=api.hashtag("hello")
    for v in api.hashtag("hello").videos():
        print("in v loop")
        print(v)
    print("videos: ",tag.videos())
    print("dict: ",tag.as_dict)
    print(tag)
'''
from TikTokApi import TikTokApi

print("start")
# Watch https://www.youtube.com/watch?v=-uCt1x8kINQ for a brief setup tutorial
with TikTokApi() as api:
    for trending_video in api.trending.videos():
        user_stats = trending_video.author.info_full['stats']
        print(user_stats)
        
print("end")
