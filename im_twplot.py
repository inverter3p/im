from PIL import Image
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
# from scipy.integrate import cumtrapz

st.set_page_config(
    page_title="Induction motor Torque-speed curve",
    page_icon="🎮",
    initial_sidebar_state="expanded",
)

st.write(""" # Torqe-Speed Curve of Induction Motor """)
st.info('Simplified Equivalent Circuit')
im_eq = Image.open('simple_im.png')
st.image(im_eq,use_column_width = True)
