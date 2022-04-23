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
        st.image(image, caption='News in 60 seconds or less')
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
    return df


def generate_summary(sample_df, i):
    st.image(sample_df.iloc[i]['img_link'], width=500)
    st.write(sample_df.iloc[i]['Title'])
    st.write(sample_df.iloc[i]['summary'])
    st.write("Source : " + (sample_df.iloc[i]['Source']))
    st.write("Original Post : " + (sample_df.iloc[i]['link']))
    comp = 100 - round(len(sample_df.iloc[i]['summary']) * 100 / len(sample_df.iloc[i]['news']), 2)
    time_saved = len(sample_df.iloc[i]['news']) // 250 - len(sample_df.iloc[i]['summary']) // 250
    st.success(
        "Length of original article : {} \n\n "
        "Length of summarized article : {} \n\n"
        "Compression : {}% \n\n "
        "You saved {} minutes".format(
            len(sample_df.iloc[i]['news']), len(sample_df.iloc[i]['summary']), comp, time_saved)
    )


def main():
    setup_streamlit()
    df = load_text_generator()
    col1, col2, col3 = st.columns([7, 4, 5])
    with col1:
        st.write(' ')
    with col2:
        news_button = st.button('Summarize News')
    with col3:
        st.write(' ')

    st.markdown(
        "<hr />",
        unsafe_allow_html=True
    )
    if news_button:
        sample_df = df.sample(n=10)
        utils.append_df(sample_df)
        for i in range(10):
            col1, col2 = st.columns([2, 10])
            with col1:
                st.image(sample_df.iloc[i]['img_link'], width=200)
            with col2:
                st.subheader(sample_df.iloc[i]['Title'])
                if i == 0:
                    b0 = st.button('Read More', key=i)
                    if b0:
                        utils.append_button_list(i)
                elif i == 1:
                    b1 = st.button('Read More', key=i)
                    if b1:
                        utils.append_button_list(i)
                elif i == 2:
                    b2 = st.button('Read More', key=i)
                    if b2:
                        utils.append_button_list(i)
                elif i == 3:
                    b3 = st.button('Read More', key=i)
                    if b3:
                        utils.append_button_list(i)
                elif i == 4:
                    b4 = st.button('Read More', key=i)
                    if b4:
                        utils.append_button_list(i)
                elif i == 5:
                    b5 = st.button('Read More', key=i)
                    if b5:
                        utils.append_button_list(i)
                elif i == 6:
                    b6 = st.button('Read More', key=i)
                    if b6:
                        utils.append_button_list(i)
                elif i == 7:
                    b7 = st.button('Read More', key=i)
                    if b7:
                        utils.append_button_list(i)
                elif i == 8:
                    b8 = st.button('Read More', key=i)
                    if b8:
                        utils.append_button_list(i)
                elif i == 9:
                    b9 = st.button('Read More', key=i)
                    if b9:
                        utils.append_button_list(i)

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
                st.subheader(sample_df.iloc[i]['Title'])
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


if __name__ == '__main__':
    main()
