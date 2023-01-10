import streamlit as st
import cv2
import numpy as np

st.title('12bit to 8bit Gamma Correction')

# ファイルをアップロードする
uploaded_file = st.file_uploader('Choose a file')

# ファイルがアップロードされた場合
if uploaded_file is not None:
    # ファイルをバイナリとして読み込む
    image_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)

    # バイナリから画像を読み込む
    image = cv2.imdecode(image_bytes, -1)

    # 画像をfloat32型に変換する
    image = image.astype(np.float32)

    # gamma補正の指数を入力する
    gamma = st.slider('Gamma', 0.010, 10, 0.040, 0.001)

    # gamma補正を行う
    image = np.power(image / np.max(image), gamma) * np.max(image)

    # 画像をuint8型に変換する
    image = image.astype(np.uint8)

    # 画像を表示する
    st.image(image, width=500)
