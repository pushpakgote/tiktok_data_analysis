import streamlit as st
from subprocess import call
from pathlib import Path
import pandas as pd

#download
st.download_button(
    label="Download JSON",
    file_name="data.json",
    mime="application/json",
    data=Path("tiktok_json.json").read_text(),
)


#input
hashtag1=st.text_input('Search hashtags . . .',value="0")

if st.button('Get Data 1'):
    st.write(hashtag1)
    call(hashtag1.split(' '))
    #call(['python','tiktok.py',hashtag])
    #with open('test.txt') as f:
    #    contents = f.read()
    #st.write(contents)
    
hashtag=st.text_input('Search hashtags . . .',value="1")

if st.button('Get Data'):
    st.write(hashtag)
    call(['python','tiktok.py',hashtag])
    df=pd.read_csv('processed_tiktok.csv')
    df

