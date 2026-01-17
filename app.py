import streamlit as st
import platform
from data.setup_steps import setup_steps

st.set_page_config(page_title="Setup Buddy", page_icon="🚀", layout="wide")

# Styling
st.markdown("""
<style>
    .big-font {font-size:20px !important; line-height:1.6;}
    .title {font-size:42px !important; font-weight:bold; color:#1E88E5;}
</style>
""", unsafe_allow_html=True)

# OS detection
os_name = platform.system()
is_windows = os_name == "Windows"

# Title
st.markdown('<p class="title">Setup Buddy</p>', unsafe_allow_html=True)
st.markdown("### Guided setup for Luigi Workshop – use arrows or sidebar to navigate!")

# Sidebar: Step list menu
st.sidebar.header("Jump to Step")
for i, step in enumerate(setup_steps):
    label = step["title"]
    if i == st.session_state.get('current_step', 0):
        label = f"**{label}** ← Current"
    if st.sidebar.button(label, key=f"jump_{i}"):
        st.session_state.current_step = i
        st.rerun()

# Step tracking
if 'current_step' not in st.session_state:
    st.session_state.current_step = 0

step = setup_steps[st.session_state.current_step]

# Progress
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

# Navigation buttons
col1, col2 = st.columns(2)
if col1.button("⬅️ Previous Step"):
    if st.session_state.current_step > 0:
        st.session_state.current_step -= 1
        st.rerun()

if col2.button("Next Step ➡️"):
    if st.session_state.current_step < total - 1:
        st.session_state.current_step += 1
        st.rerun()
    else:
        st.balloons()
        st.success("All done! You're workshop-ready 🎉")

# Help button
if st.button("❓ Stuck? Show Help"):
    with st.expander("Fixes for this step", expanded=True):
        for tip in step.get("troubleshooting", []):
            st.markdown(f"- {tip}")

# Keyboard navigation (arrow keys)
st.markdown("""
<script>
const doc = window.parent.document;
doc.addEventListener('keydown', function(e) {
    if (e.key === 'ArrowLeft') {
        document.querySelector('[data-testid="stButton"][aria-label*="Previous"]').click();
    } else if (e.key === 'ArrowRight') {
        document.querySelector('[data-testid="stButton"][aria-label*="Next"]').click();
    }
});
</script>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("Made for Luigi Solutions Workshop • Jan 17, 2026 • Nick Wedra")