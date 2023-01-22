import streamlit as st
import cv2
import numpy as np
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


st.title('12bit to 8bit Gamma Correction')

# ファイルをアップロードする
uploaded_file = st.file_uploader('Choose a file')

# ファイルがアップロードされた場合
if uploaded_file is not None:
    # Open the image
    im = Image.open(uploaded_file)

    # Convert the image to numpy array
    img = np.array(im)
    img_log = np.array(img)

    
    # gamma補正の指数を入力する
    gamma = st.slider('Gamma', 0.010, 0.09, 0.040, 0.001)

    img_log = np.power(img_log / img_log[0].max(), gamma) * img_log[0].max()

    im = Image.fromarray(img_log/img_log[0].max()*255)
    #plt.imshow(im)
    #plt.show()

    # 画像を表示する
    st.image(image, width=500)
