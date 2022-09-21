import streamlit as st
from subprocess import call

#input
hashtag=st.text_input('Search hashtags . . .',value="")

if st.button('Get Data'):
    st.write(hashtag)
    call(['python','tiktok.py',hashtag])
    with open('test.txt') as f:
        contents = f.read()
    st.write(contents)
    
    print('Print :',contents)


