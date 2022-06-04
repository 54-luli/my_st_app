import streamlit as st
import os
from streamlit.elements.image import image_to_url

PWD = os.path.dirname(__file__)


def background():
    photo_path = os.path.join(PWD, 'files/image/mountain.jpg')
    # 加载背景图
    img_url = image_to_url(photo_path, width=1280, clamp=False, channels='RGB', output_format='auto',
                           image_id='', allow_emoji=False)
    st.markdown('''
    <style>
    .css-fg4pbf {background-image: url(''' + img_url + ''');}</style>
    ''', unsafe_allow_html=True)
