import streamlit as st
import pandas as pd
from personal_ia import *

st.set_page_config(layout="wide")

personalia = PersonalIA("video_frente.mp4")
personalia.run()

while True:
    frame, results = personalia.image_q.get()
    st.image()