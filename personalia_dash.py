import streamlit as st
import pandas as pd
from personal_ia import *

st.set_page_config(layout="wide")

personalia = PersonalIA("video_frente.mp4")
personalia.run(draw=True, display=False)

placeholder = st.empty()
count = 0
status = "relexed"
while True:
    frame, landmarks, ts = personalia.image_q.get()

    if len(landmarks.pose_landmarks) > 0:

        frame, elbow_angle = personalia.find_angle(frame, landmarks, 12, 14, 16, True)
        frame, hip_angle = personalia.find_angle(frame, landmarks, 11, 23, 25, True)

        if elbow_angle > 150 and hip_angle > 170:
            status = "ready"
            dir = "down"
        if status == "ready":
            if dir == "down" and elbow_angle < 60:
                dir = "up"
                count += 0.5
            if dir == "up" and elbow_angle > 100:
                dir = "down"
                count += 0.5

        with placeholder.container():
            col1, col2 = st.columns([0.4, 0.6])
            col1.image(frame)

            col2.markdown("### **Status:**" + status)
            col2.markdown(f"## Count: {int(count)}")
