
import streamlit as st

st.set_page_config(page_title="Dragon Theme", layout="centered")

# Load CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("""
<div class="mobile">

<div class="status-bar">
<span>9:41</span>
<span>DragonNet 🔋</span>
</div>

<div class="wallpaper">

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
</div>

<div class="dock">

<img src="https://cdn-icons-png.flaticon.com/512/724/724664.png">
<img src="https://cdn-icons-png.flaticon.com/512/561/561127.png">
<img src="https://cdn-icons-png.flaticon.com/512/747/747376.png">
<img src="https://cdn-icons-png.flaticon.com/512/888/888879.png">

</div>

</div>
""", unsafe_allow_html=True)
