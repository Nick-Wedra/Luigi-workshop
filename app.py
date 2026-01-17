import streamlit as st
import platform
from data.setup_steps import setup_steps  # Your steps from earlier

st.set_page_config(page_title="Setup Buddy", page_icon="🚀", layout="wide")

# Styling
st.markdown("""
<style>
    .big-font {font-size:20px !important; line-height:1.6;}
    .title {font-size:42px !important; font-weight:bold; color:#1E88E5;}
</style>
""", unsafe_allow_html=True)

# OS detection (for commands)
os_name = platform.system()
is_windows = os_name == "Windows"

# Title
st.markdown('<p class="title">Setup Buddy</p>', unsafe_allow_html=True)
st.markdown("### Guided setup for Luigi Workshop – Windows/Mac friendly!")

# Tabs: Checklist + Debug
tabs = st.tabs(["Setup Checklist", "Debug Helper"])

# Tab 1: Setup Checklist (your existing wizard)
with tabs[0]:
    if 'current_step' not in st.session_state:
        st.session_state.current_step = 0

    step = setup_steps[st.session_state.current_step]

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

    col1, col2 = st.columns(2)
    if col1.button("✅ Done – Next Step"):
        if st.session_state.current_step < len(setup_steps) - 1:
            st.session_state.current_step += 1
            st.rerun()
        else:
            st.balloons()
            st.success("All done! You're workshop-ready 🎉")

    if col2.button("❓ Stuck? Show Help"):
        with st.expander("Common Fixes for this step", expanded=True):
            for tip in step.get("troubleshooting", []):
                st.markdown(f"- {tip}")

    if st.session_state.current_step > 0:
        if st.button("⬅️ Back"):
            st.session_state.current_step -= 1
            st.rerun()

# Tab 2: Debug Helper (new!)
with tabs[1]:
    st.header("Debug Helper")
    st.write("Common setup errors & fixes – click to expand each category.")

    with st.expander("Python Installation Issues"):
        st.markdown("- **'python' is not recognized** → Reinstall Python from python.org and check 'Add Python to PATH'. Restart terminal.")
        st.markdown("- **Microsoft Store opens instead** → Settings → Apps → App execution aliases → turn OFF python.exe and python3.exe.")
        st.markdown("- **Wrong/old version** → Uninstall old Python versions (Settings → Apps → search Python), then install 3.10+.")
        st.markdown("- **Mac: 'python' not found** → Use `python3` instead, or install via python.org/brew.")

    with st.expander("Venv Creation/Activation Problems"):
        st.markdown("- **Permission denied** → Run PowerShell as administrator (Windows) or use sudo (Mac – rare).")
        st.markdown("- **Scripts disabled on Windows** → Run once: `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`")
        st.markdown("- **No (venv) prompt after activation** → Wrong folder – make sure you're in the project folder with venv inside.")
        st.markdown("- **Mac/Linux activation fails** → Use `source venv/bin/activate` exactly.")

    with st.expander("Streamlit / Pip Errors"):
        st.markdown("- **pip or streamlit not found** → Venv not active – run activation command again.")
        st.markdown("- **Install slow or fails** → Run `pip install --upgrade pip` first, then retry.")
        st.markdown("- **Browser doesn't open** → Manually visit http://localhost:8501.")
        st.markdown("- **Port in use** → Close other apps or run `streamlit hello --server.port 8502`.")

    st.write("Still stuck? Paste your error here and copy the prompt to ChatGPT:")
    error = st.text_area("Paste your exact error message:", height=120)
    if st.button("Generate AI Prompt"):
        if error.strip():
            prompt = f"During Luigi workshop setup, I got this error:\n{error}\nWhat does it mean and how do I fix it step by step?"
            st.code(prompt, language="text")
            st.info("Copy the prompt above and paste into ChatGPT!")
        else:
            st.warning("Paste an error first!")

# Footer
st.markdown("---")
st.caption("Made for Luigi Solutions Workshop • Jan 17, 2026 • Nick Wedra")