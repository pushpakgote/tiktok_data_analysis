from TikTokApi import TikTokApi

print("inside test.py")
# Watch https://www.youtube.com/watch?v=-uCt1x8kINQ for a brief setup tutorial
with TikTokApi() as api:
    print("inside 1st loop")
    #for trending_video in api.trending.videos(count=20):
    tag=api.hashtag("hello")
    for v in tag.videos():
        print("in v loop")
        print(v.as_dict)
    print("videos: ",tag.videos())
    print("dict: ",tag.as_dict)
    print(tag)
