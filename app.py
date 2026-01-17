import streamlit as st
import platform
from data.setup_steps import setup_steps  # Your steps list

st.set_page_config(page_title="Setup Buddy", page_icon="🚀", layout="wide")

# Styling (clean, modern)
st.markdown("""
<style>
    .big-font {font-size:22px !important; line-height:1.8;}
    .title {font-size:48px !important; font-weight:300; color:#007aff; letter-spacing:1px;}
    .stButton > button {
        background-color: #007aff;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 20px;
        font-size: 18px;
    }
    .stButton > button:hover {
        background-color: #005bb5;
    }
    .sidebar .stButton > button {width: 100%; text-align: left;}
</style>
""", unsafe_allow_html=True)

# OS detection
os_name = platform.system()
is_windows = os_name == "Windows"

st.sidebar.write(f"**Detected OS:** {os_name}")

# Title
st.markdown('<p class="title">Setup Buddy</p>', unsafe_allow_html=True)
st.markdown("### Guided setup for Luigi Workshop – click any step to jump")

# Sidebar: Full list view of all steps (clickable)
st.sidebar.header("All Steps")
current = st.session_state.get('current_step', 0)
for i, step in enumerate(setup_steps):
    label = step["title"]
    if i == current:
        label = f"→ {label}"
    if st.sidebar.button(label, key=f"jump_{i}", use_container_width=True):
        st.session_state.current_step = i
        st.rerun()

# Step tracking
if 'current_step' not in st.session_state:
    st.session_state.current_step = 0

step = setup_steps[st.session_state.current_step]

# Progress bar (modern, thin)
total = len(setup_steps)
st.progress(st.session_state.current_step / total)
st.caption(f"Step {st.session_state.current_step + 1} of {total}")

# Main content
st.header(step["title"])
st.markdown(f'<p class="big-font">{step["instructions"]}</p>', unsafe_allow_html=True)

if step.get("link"):
    st.link_button("Open Link", step["link"])

if step.get("command"):
    cmd = step["command"]
    if not is_windows:
        cmd = cmd.replace("python", "python3").replace("\\", "/")
    lang = "powershell" if is_windows else "bash"
    st.code(cmd, language=lang)

# Bottom navigation buttons
col1, col2 = st.columns(2)
with col1:
    if st.session_state.current_step > 0:
        if st.button("⬅️ Previous"):
            st.session_state.current_step -= 1
            st.rerun()

with col2:
    if st.button("Next ➡️"):
        if st.session_state.current_step < total - 1:
            st.session_state.current_step += 1
            st.rerun()
        else:
            st.balloons()
            st.success("All done! You're workshop-ready 🎉")

# Step-specific help
if st.button("❓ Stuck? Show Help"):
    with st.expander("Fixes for this step", expanded=True):
        for tip in step.get("troubleshooting", []):
            st.markdown(f"- {tip}")

# Footer
st.markdown("---")
st.caption("Made for Luigi Solutions Workshop • Jan 17, 2026 • Nick Wedra")