import praw
import pandas as pd
import reddit_api
from model_prediction import predict_sentiment

# Instance of Reddit
reddit = praw.Reddit(
    client_id     = reddit_api.client_id,
    client_secret = reddit_api.client_secret,
    user_agent    = reddit_api.user_agent
)

# subreddit to extract posts from
def fetch_posts(subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)

    titles = []
    scores = []

    for submission in subreddit.top(limit=50):
        titles.append(submission.title)
        scores.append(submission.score)
    
    return titles, scores