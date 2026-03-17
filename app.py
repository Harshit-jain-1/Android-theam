# app.py
import streamlit as st
import base64

st.set_page_config(page_title="Dragon Mobile", layout="centered")

with open("theme_data.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def load_file(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

video = load_file("5b615f3f74e1a3369f184065fba10bbd.mp4")

st.markdown(f"""
<div class="mobile">
<div class="wallpaper">

<video autoplay muted loop class="dragon-video">
<source src="data:video/mp4;base64,{video}" type="video/mp4">
</video>

<div class="status-bar">
<span>9:41</span>
<span>DragonNet 🔋</span>
</div>

<div class="clock">
<h1>09:41</h1>
<p>Dragon Kingdom</p>
</div>

<div class="apps">
<div class="app"><video autoplay muted loop class="icon-video"><source src="data:video/mp4;base64,{video}"></video><p>Phone</p></div>
<div class="app"><video autoplay muted loop class="icon-video"><source src="data:video/mp4;base64,{video}"></video><p>Messages</p></div>
<div class="app"><video autoplay muted loop class="icon-video"><source src="data:video/mp4;base64,{video}"></video><p>Settings</p></div>
<div class="app"><video autoplay muted loop class="icon-video"><source src="data:video/mp4;base64,{video}"></video><p>Camera</p></div>
<div class="app"><video autoplay muted loop class="icon-video"><source src="data:video/mp4;base64,{video}"></video><p>Chrome</p></div>
<div class="app"><video autoplay muted loop class="icon-video"><source src="data:video/mp4;base64,{video}"></video><p>Gallery</p></div>
<div class="app"><video autoplay muted loop class="icon-video"><source src="data:video/mp4;base64,{video}"></video><p>Music</p></div>
<div class="app"><video autoplay muted loop class="icon-video"><source src="data:video/mp4;base64,{video}"></video><p>Files</p></div>
</div>

<div class="dock">
<video autoplay muted loop class="dock-video"><source src="data:video/mp4;base64,{video}"></video>
<video autoplay muted loop class="dock-video"><source src="data:video/mp4;base64,{video}"></video>
<video autoplay muted loop class="dock-video"><source src="data:video/mp4;base64,{video}"></video>
<video autoplay muted loop class="dock-video"><source src="data:video/mp4;base64,{video}"></video>
</div>

</div>
</div>
""", unsafe_allow_html=True)
