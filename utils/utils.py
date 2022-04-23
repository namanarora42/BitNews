df_list = []


def clear_all():
    df_list.clear()


def append_df(df):
    df_list.append(df)


def get_df():
    if len(df_list) == 0:
        return []
    return df_list[-1]
