df_list = []
news_disp = []


def clear_all():
    df_list.clear()
    news_disp.clear()


def append_df(df):
    df_list.clear()
    df_list.append(df)


def append_news(news):
    news_disp.clear()
    news_disp.append(news)


def get_df():
    if len(df_list) == 0:
        return []
    return df_list[-1]


def get_news_disp():
    if len(news_disp) == 0:
        return []
    return news_disp[-1]
