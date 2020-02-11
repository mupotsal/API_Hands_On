#Look here for praw documentation: https://praw.readthedocs.io/en/latest/code_overview/praw_models.html
import praw
import redditinfo
import word 

reddit = praw.Reddit(client_id=redditinfo.CLIENT_ID,
                     client_secret= redditinfo.CLIENT_SECRET,
                     password = redditinfo.PASSWORD,
                     user_agent= redditinfo.USER_AGENT,
                     username = redditinfo.USERNAME)

subreddit = reddit.subreddit("USA") #Your subreddit name here

#You can pick any number of newest or top post titles
#newest = subreddit.new(limit = 1000)
top = subreddit.top(limit = 400)

f = open("output.txt", "w+")
try:
    for post in top:
        text = post.title.encode('ascii', 'ignore')  # ignores any character that isn't ascii
        decoded = text.decode()  # changes from bytes to string
        f.write(decoded + ", \n")  # writes to file
except IOError:
    print("Something went wrong. :(")



f.close()
word.main("output.txt")
