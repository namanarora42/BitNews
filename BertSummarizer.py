import pandas as pd
import torch
from summarizer import Summarizer

model = Summarizer('distilbert-base-uncased')
df = pd.read_csv("data/raw_news_new.csv")
df.columns = ['title', 'news', 'author', 'link', 'img_link', 'Source']
df.drop_duplicates(subset='title', inplace=True)


def f(x):
    resp = model(x['news'], ratio=0.1)
    return resp


df['summary'] = df.apply(lambda x: f(x), axis=1)

df.to_csv('data/processed_news', index=False)
