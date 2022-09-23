import streamlit as st
from subprocess import call
from pathlib import Path

#download
st.download_button(
    label="Download JSON",
    file_name="data.json",
    mime="application/json",
    data=Path("tiktok_json.json").read_text(),
)


#input
hashtag=st.text_input('Search hashtags . . .',value="")

if st.button('Get Data'):
    st.write(hashtag)
    call(hashtag.split(' '))
    #call(['python','tiktok.py',hashtag])
    with open('test.txt') as f:
        contents = f.read()
    #st.write(contents)
    
    print('Print :',contents)

