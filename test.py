from TikTokApi import TikTokApi

print("inside test.py")
# Watch https://www.youtube.com/watch?v=-uCt1x8kINQ for a brief setup tutorial
with TikTokApi() as api:
    print("inside 1st loop")
    #for trending_video in api.trending.videos(count=20):
    for trending_video in api.hashtag("hello"):
        # Prints the author's username of the trending video.
        print(trending_video)
