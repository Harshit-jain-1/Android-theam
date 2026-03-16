
import streamlit as st
import pandas as pd
import io

from sklearn.tree import DecisionTreeClassifier

from dragon_lion_generator import generate_theme


# ---------------------------
# PAGE CONFIG
# ---------------------------

st.set_page_config(
    page_title="Dragon Lion Theme Generator",
    page_icon="🐉",
    layout="centered"
)

st.title("🐉🦁 Dragon + Lion Mobile Theme Generator")


# ---------------------------
# LOAD DATA
# ---------------------------

data = pd.read_csv("theme_data.csv")

X = data[["color_r","color_g","color_b"]]

y = data["theme"]


# ---------------------------
# TRAIN MODEL
# ---------------------------

model = DecisionTreeClassifier()

model.fit(X,y)


# ---------------------------
# USER INPUT
# ---------------------------

st.sidebar.header("Select Theme Colors")

r = st.sidebar.slider("Red",0,255,150)

g = st.sidebar.slider("Green",0,255,80)

b = st.sidebar.slider("Blue",0,255,50)


# ---------------------------
# PREDICT THEME
# ---------------------------

prediction = model.predict([[r,g,b]])

theme = prediction[0]

st.subheader("Predicted Theme")

st.success(theme)


# ---------------------------
# GENERATE WALLPAPER
# ---------------------------

image = generate_theme(r,g,b)

st.subheader("Wallpaper Preview")

st.image(image,use_container_width=True)


# ---------------------------
# DOWNLOAD WALLPAPER
# ---------------------------

buffer = io.BytesIO()

image.save(buffer,format="PNG")

st.download_button(
label="Download Wallpaper",
data=buffer.getvalue(),
file_name="dragon_lion_theme.png",
mime="image/png"
)


# ---------------------------
# THEME DESCRIPTION
# ---------------------------

st.subheader("Theme Description")

if "dragon" in theme:
    st.write("🔥 Powerful Dragon Dark Theme")

elif "lion" in theme:
    st.write("🦁 Royal Lion Golden Theme")


st.write("---")

st.caption("AI Mobile Theme Generator using Streamlit + Machine Learning")
