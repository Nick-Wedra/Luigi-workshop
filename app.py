import streamlit as st
import platform

# Fake your steps list for now (replace with real import later)
setup_steps = [
    {"title": "Step 1: Install VS Code", "instructions": "Download from https://code.visualstudio.com"},
    {"title": "Step 2: Install Python", "instructions": "Get Python 3.10+ from python.org"},
    {"title": "Step 3: Create Venv", "instructions": "Run: python -m venv venv"},
    {"title": "Step 4: Activate Venv", "instructions": "Run: venv\\Scripts\\activate (Windows) or source venv/bin/activate (Mac)"},
    {"title": "All Done!", "instructions": "You're ready for the workshop!"}
]

st.set_page_config(page_title="Setup Buddy", page_icon="🚀", layout="wide")

# Detect OS
os_name = platform.system()
is_windows = os_name == "Windows"

st.title("Setup Buddy")
st.markdown("### Get ready for the Luigi Workshop in minutes – step by step!")

# Session state for current step
if 'current_step' not in st.session_state:
    st.session_state.current_step = 0

step = setup_steps[st.session_state.current_step]

st.header(step["title"])
st.write(step["instructions"])

# OS-specific command example
if "Activate Venv" in step["title"]:
    cmd = "venv\\Scripts\\activate" if is_windows else "source venv/bin/activate"
    st.code(cmd, language="powershell" if is_windows else "bash")

col1, col2 = st.columns(2)
if col1.button("✅ Done – Next Step"):
    if st.session_state.current_step < len(setup_steps) - 1:
        st.session_state.current_step += 1
        st.rerun()
    else:
        st.success("All done! You're workshop-ready! 🎉")
        st.balloons()

if col2.button("❓ Stuck? Show Help"):
    st.info("Common fixes coming soon...")

# Back button
if st.session_state.current_step > 0:
    if st.button("⬅️ Back"):
        st.session_state.current_step -= 1
        st.rerun()

st.markdown("---")
st.caption("Made for Luigi Solutions Workshop • Jan 17, 2026 • Nick Wedra")