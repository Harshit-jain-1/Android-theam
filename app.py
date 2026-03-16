# app.py

import streamlit as st
import base64

st.set_page_config(
    page_title="Dragon Mobile Theme",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# load css
with open("theme_data.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# convert video to base64
def load_video(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

video = load_video("5b615f3f74e1a3369f184065fba10bbd.mp4")

st.markdown(f"""
<video autoplay muted loop class="video-bg">
<source src="data:video/mp4;base64,{video}" type="video/mp4">
</video>
""", unsafe_allow_html=True)

st.markdown("""

<div class="mobile">

<div class="status-bar">
<span>9:41</span>
<span>DragonNet 🔋</span>
</div>

<div class="clock">
<h1>09:41</h1>
<p>Dragon Kingdom</p>
</div>

<div class="apps">

<div class="app">
<img src="https://cdn-icons-png.flaticon.com/512/724/724664.png">
<p>Phone</p>
</div>

<div class="app">
<img src="https://cdn-icons-png.flaticon.com/512/561/561127.png">
<p>Messages</p>
</div>

<div class="app">
<img src="https://cdn-icons-png.flaticon.com/512/1828/1828919.png">
<p>Settings</p>
</div>

<div class="app">
<img src="https://cdn-icons-png.flaticon.com/512/747/747376.png">
<p>Camera</p>
</div>

<div class="app">
<img src="https://cdn-icons-png.flaticon.com/512/732/732200.png">
<p>Chrome</p>
</div>

<div class="app">
<img src="https://cdn-icons-png.flaticon.com/512/888/888879.png">
<p>Gallery</p>
</div>

<div class="app">
<img src="https://cdn-icons-png.flaticon.com/512/2920/2920244.png">
<p>Music</p>
</div>

<div class="app">
<img src="https://cdn-icons-png.flaticon.com/512/1827/1827392.png">
<p>Files</p>
</div>

</div>

<div class="dock">
<img src="https://cdn-icons-png.flaticon.com/512/724/724664.png">
<img src="https://cdn-icons-png.flaticon.com/512/561/561127.png">
<img src="https://cdn-icons-png.flaticon.com/512/747/747376.png">
<img src="https://cdn-icons-png.flaticon.com/512/888/888879.png">
</div>

</div>

""", unsafe_allow_html=True)
