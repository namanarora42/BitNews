import pandas as pd
import streamlit as st
from PIL import Image

from utils import utils


def setup_streamlit():
    st.set_page_config(page_title="BitNews", layout="wide", page_icon="🗞️️")
    image = Image.open('assets/logo2.png')

    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(' ')
    with col2:
        st.image(image, caption='Bits of News That Matter')
    with col3:
        st.write(' ')

    st.markdown(
        """
        <style>
        [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
            width: 400px;
        }
        [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
            width: 400px;
            margin-left: -400px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


@st.cache(allow_output_mutation=True)
def load_text_generator():
    df = pd.read_csv("data/processed_news.csv")
    df.drop_duplicates(inplace=True)

    def f(x):
        return int(len(x['summary']) // 250)

    df['time_per_art'] = df.apply(lambda x: f(x), axis=1)
    return df


def generate_summary(sample_df, i):
    st.image(sample_df.iloc[i]['img_link'], width=500)
    st.write(sample_df.iloc[i]['title'])
    st.write(sample_df.iloc[i]['summary'])
    st.write("Source : " + (sample_df.iloc[i]['Source']))
    st.write("Original Article : " + (sample_df.iloc[i]['link']))
    comp = 100 - round(len(sample_df.iloc[i]['summary']) * 100 // len(sample_df.iloc[i]['news']), 2)
    time_saved = len(sample_df.iloc[i]['news']) // 250 - len(sample_df.iloc[i]['summary']) // 250
    st.success(
        "Length of original article : {} \n\n "
        "Length of summarized article : {} \n\n"
        "Compression : {}% \n\n "
        "Similarity Score : {}\n\n"
        "You saved {} minutes".format(
            len(sample_df.iloc[i]['news']), len(sample_df.iloc[i]['summary']), comp,
            round(float(sample_df.iloc[i]['similarity']), 2),
            time_saved)
    )


def main():
    setup_streamlit()
    df = load_text_generator()
    try:
        st.markdown(
            """
            <style>
            [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
                width: 500px;
            }
            [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
                width: 500px;
                margin-left: -500px;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        with st.sidebar.header("Category"):
            category = st.sidebar.multiselect("Select News Category", df['category'].unique().tolist(),
                                              default=df['category'].unique().tolist())
            if category == 'All':
                category = df['category'].unique().tolist()

        with st.sidebar.header("Source"):
            source = st.sidebar.multiselect("Select News Source", df['Source'].unique().tolist(),
                                            default=df['Source'].unique().tolist())
            if source == 'All':
                source = df['Source'].unique().tolist()

        with st.sidebar.header("Number of articles"):
            num = st.sidebar.slider("No. of news articles", min_value=1, max_value=10, step=1)

        with st.sidebar.header("Time per article"):
            time_spend = st.sidebar.slider("Maximum Time you want to spend per article", min_value=1, max_value=10,
                                           step=1)
        if st.sidebar.button('Summarize News'):
            sample_df = df[df['category'].isin(category) & df['Source'].isin(source)]
            sample_df = sample_df[sample_df['time_per_art'] <= time_spend]
            sample_df = sample_df.sample(n=min(len(sample_df), num))
            utils.append_df(sample_df)
            for i in range(10):
                col1, col2 = st.columns([2, 10])
                with col1:
                    st.image(sample_df.iloc[i]['img_link'], width=200)
                with col2:
                    st.subheader(sample_df.iloc[i]['title'])
                    if i == 0:
                        b0 = st.button('Read More', key=i)
                    elif i == 1:
                        b1 = st.button('Read More', key=i)
                    elif i == 2:
                        b2 = st.button('Read More', key=i)
                    elif i == 3:
                        b3 = st.button('Read More', key=i)
                    elif i == 4:
                        b4 = st.button('Read More', key=i)
                    elif i == 5:
                        b5 = st.button('Read More', key=i)
                    elif i == 6:
                        b6 = st.button('Read More', key=i)
                    elif i == 7:
                        b7 = st.button('Read More', key=i)
                    elif i == 8:
                        b8 = st.button('Read More', key=i)
                    elif i == 9:
                        b9 = st.button('Read More', key=i)

                st.markdown("<hr />",
                            unsafe_allow_html=True)
            return sample_df
        else:
            sample_df = utils.get_df()
            if len(sample_df) == 0:
                return
            for i in range(10):
                col1, col2 = st.columns([2, 10])
                with col1:
                    st.image(sample_df.iloc[i]['img_link'], width=200)
                with col2:
                    st.subheader(sample_df.iloc[i]['title'])
                    if i == 0:
                        b0 = st.button('Read More', key=i)
                        if b0:
                            generate_summary(sample_df, i)
                    elif i == 1:
                        b1 = st.button('Read More', key=i)
                        if b1:
                            generate_summary(sample_df, i)
                    elif i == 2:
                        b2 = st.button('Read More', key=i)
                        if b2:
                            generate_summary(sample_df, i)
                    elif i == 3:
                        b3 = st.button('Read More', key=i)
                        if b3:
                            generate_summary(sample_df, i)
                    elif i == 4:
                        b4 = st.button('Read More', key=i)
                        if b4:
                            generate_summary(sample_df, i)
                    elif i == 5:
                        b5 = st.button('Read More', key=i)
                        if b5:
                            generate_summary(sample_df, i)
                    elif i == 6:
                        b6 = st.button('Read More', key=i)
                        if b6:
                            generate_summary(sample_df, i)
                    elif i == 7:
                        b7 = st.button('Read More', key=i)
                        if b7:
                            generate_summary(sample_df, i)
                    elif i == 8:
                        b8 = st.button('Read More', key=i)
                        if b8:
                            generate_summary(sample_df, i)
                    elif i == 9:
                        b9 = st.button('Read More', key=i)
                        if b9:
                            generate_summary(sample_df, i)

                st.markdown("<hr />",
                            unsafe_allow_html=True)
    except Exception:
        pass


if __name__ == '__main__':
    main()
