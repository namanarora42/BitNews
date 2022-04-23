import time

import newspaper
from newspaper import Article
import pandas as pd


class NewsParser:
    def __init__(self, source):
        self.source = source
        self.count = 0
        if source == "BBC":
            self.paper = newspaper.build('https://www.bbc.co.uk')
        elif source == "NYTimes":
            self.paper = newspaper.build('https://nytimes.com')
        elif source == "CNN":
            self.paper = newspaper.build('https://cnn.com')
        elif source == "Forbes":
            self.paper = newspaper.build('https://forbes.com')
        elif source == "Yahoo":
            self.paper = newspaper.build('https://yahoo.com')
        elif source == "Verge":
            self.paper = newspaper.build('https://www.theverge.com')
        elif source == "TechCrunch":
            self.paper = newspaper.build('https://techcrunch.com')
        elif source == "HollywoodReporter":
            self.paper = newspaper.build('https://www.hollywoodreporter.com')
        elif source == "Reuters":
            self.paper = newspaper.build('https://www.reuters.com')

    def parse(self):
        full_list = []
        num_articles = 0
        try:
            if len(self.paper.articles) == 0:
                print("Waiting for : {}".format(self.count))
                self.count += 1
                time.sleep(5)
                if self.count == 2:
                    self.count = 0
                    print("Enough wait")
                    return
                else:
                    self.parse()
            for article in self.paper.articles:
                if num_articles % 2 == 0:
                    print("Cached news articles = {}".format(num_articles))
                news = Article(article.url)
                news.download()
                news.parse()
                if len(news.title) == 0 or len(news.text) < 50 or len(article.url) == 0 or len(news.top_img) == 0:
                    time.sleep(0.42)
                    continue
                full_list.append([news.title, news.text, ", ".join(news.authors), article.url, news.top_img, self.source])
                df = pd.DataFrame(full_list)
                # df.columns = ["title", "text", "authors", "url", "img", "source"]
                df.to_csv("data/raw_news_new.csv", index=False, mode='a', header=False)
                full_list = []
                num_articles += 1
                if num_articles == 20:
                    break
                time.sleep(0.42)
        except Exception as e:
            print(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")
            pass


if __name__ == '__main__':
    source_list = ["Verge", "CNN", "BBC", "NYTimes", "Yahoo", "Forbes", "TechCrunch", "HollywoodReporter",
                   "Reuters"]
    for source in source_list:
        print("Parsing News source : {}".format(source))
        np = NewsParser(source)
        np.parse()
