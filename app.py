import streamlit as st
import platform
from data.setup_steps import setup_steps

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(
    page_title="Setup Buddy",
    page_icon="🚀",
    layout="wide"
)

# --------------------------------------------------
# Styling
# --------------------------------------------------
st.markdown(
    """
    <style>
        .big-font {font-size:22px !important; line-height:1.8;}
        .title {font-size:48px !important; font-weight:300; color:#007aff;}
        .stButton > button {
            background-color: #007aff;
            color: white;
            border-radius: 8px;
            border: none;
            padding: 10px 20px;
            font-size: 18px;
        }
        .stButton > button:hover {background-color: #005bb5;}
        .sidebar .stButton > button {width: 100%; text-align: left;}
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# Session state init
# --------------------------------------------------
if "current_step" not in st.session_state:
    st.session_state.current_step = 0

current = st.session_state.current_step

# --------------------------------------------------
# OS detection
# --------------------------------------------------
os_name = platform.system()
is_windows = os_name == "Windows"

st.sidebar.write(f"Detected OS: **{os_name}**")

# --------------------------------------------------
# Title & intro
# --------------------------------------------------
st.markdown('<p class="title">Setup Buddy</p>', unsafe_allow_html=True)
st.caption("Turn setup friction into a guided, step-by-step flow.")
st.markdown("### Guided setup for Luigi Workshop — follow the steps below")

# --------------------------------------------------
# Sidebar navigation
# --------------------------------------------------
st.sidebar.header("All Steps")
for i, step in enumerate(setup_steps):
    label = step["title"]
    if i == current:
        label = f"→ {label}"
    if st.sidebar.button(label, key=f"jump_{i}"):
        st.session_state.current_step = i
        st.rerun()

# --------------------------------------------------
# Current step
# --------------------------------------------------
step = setup_steps[current]
total = len(setup_steps)

# Progress
st.progress((current + 1) / total)
st.caption(f"Step {current + 1} of {total}")

# --------------------------------------------------
# Main content
# --------------------------------------------------
st.header(step["title"])
st.markdown(
    f'<p class="big-font">{step["instructions"]}</p>',
    unsafe_allow_html=True
)

if step.get("image"):
    st.image(
        step["image"],
        use_column_width=True,
        caption="What this should look like"
    )

if step.get("command"):
    cmd = step["command"]
    if not is_windows:
        cmd = cmd.replace("python", "python3").replace("\\", "/")
    lang = "powershell" if is_windows else "bash"
    st.code(cmd, language=lang)

# --------------------------------------------------
# Help / troubleshooting
# --------------------------------------------------
if st.button("❓ Stuck? Show Help"):
    with st.expander("Fixes for this step", expanded=True):
        for tip in step.get("troubleshooting", []):
            st.markdown(f"- {tip}")

# --------------------------------------------------
# Navigation buttons
# --------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    if current > 0:
        if st.button("⬅️ Previous"):
            st.session_state.current_step -= 1
            st.rerun()

with col2:
    if current < total - 1:
        if st.button("Next ➡️"):
            st.session_state.current_step += 1
            st.rerun()
    else:
        st.balloons()
        st.success("All done! You're workshop-ready 🎉")
        st.info("Next up: open the starter project and begin building 🚀")

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.caption("Made for Luigi Solutions Workshop • Jan 17, 2026")
