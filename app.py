import streamlit as st
import platform

# Your steps list – expanded with AI first, full troubleshooting
setup_steps = [
    {
        "title": "Step 0: Set Up ChatGPT (Recommended First!)",
        "instructions": "Since many here are great with AI, start with ChatGPT – your coding helper!",
        "link": "https://chatgpt.com",
        "command": None,
        "troubleshooting": [
            "Can't access? Use incognito mode or check internet.",
            "New to prompting? Try: 'Explain how to set up Python venv for beginners'",
            "Need help with errors? Copy-paste them here and ask ChatGPT!"
        ]
    },
    {
        "title": "Step 1: Install VS Code",
        "instructions": "Download VS Code – our main code editor.",
        "link": "https://code.visualstudio.com/download",
        "command": None,
        "troubleshooting": [
            "Already have it? Open and skip.",
            "Download stuck? Try direct link or different browser.",
            "Install fails? Run as admin (Windows) or check permissions (Mac)."
        ]
    },
    {
        "title": "Step 2: Install Python 3.10+",
        "instructions": "Get Python from python.org. Windows: Check 'Add to PATH'!",
        "link": "https://www.python.org/downloads/",
        "command": "python --version" if platform.system() == "Windows" else "python3 --version",
        "troubleshooting": [
            "Command not found? Reinstall with PATH checked (Windows) or use 'python3' (Mac).",
            "Microsoft Store opens? Disable Python aliases in Settings > Apps.",
            "Wrong version? Uninstall old one first."
        ]
    },
    {
        "title": "Step 3: Create Virtual Environment",
        "instructions": "Create a clean venv for the project.",
        "command": "python -m venv venv" if platform.system() == "Windows" else "python3 -m venv venv",
        "troubleshooting": [
            "Permission denied? Run as admin (Windows) or sudo (Mac).",
            "Already exists? Delete old venv folder and retry.",
            "Module not found? Python too old – reinstall 3.8+."
        ]
    },
    {
        "title": "Step 4: Activate Virtual Environment",
        "instructions": "Activate – look for (venv) in your prompt.",
        "command": "venv\\Scripts\\activate" if platform.system() == "Windows" else "source venv/bin/activate",
        "troubleshooting": [
            "Windows error: 'cannot load because running scripts disabled'? Run once: Set-ExecutionPolicy RemoteSigned -Scope CurrentUser",
            "No (venv) prompt? Wrong folder – cd back and retry.",
            "Mac issue? Use source command above."
        ]
    },
    {
        "title": "Step 5: Install Streamlit & Pandas",
        "instructions": "Install the workshop tools (venv must be active).",
        "command": "pip install streamlit pandas",
        "troubleshooting": [
            "pip not found? Reactivate venv.",
            "Slow/error? Run pip install --upgrade pip first.",
            "Version conflict? Use Python 3.8–3.12 (3.14 is experimental)."
        ]
    },
    {
        "title": "Step 6: Test Everything",
        "instructions": "Run this – browser should open a demo!",
        "command": "streamlit hello",
        "troubleshooting": [
            "Streamlit not found? Venv not active – activate again.",
            "Browser not opening? Manually go to http://localhost:8501",
            "Port busy? Use streamlit hello --server.port 8502"
        ]
    }
]

# Page config
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

# Sidebar info
st.sidebar.header("Info")
st.sidebar.write(f"Detected OS: **{os_name}**")
st.sidebar.caption("Made for Luigi Workshop • Jan 17, 2026")

# Title
st.markdown('<p class="title">Setup Buddy</p>', unsafe_allow_html=True)
st.write("Step-by-step guide for Windows & Mac – with AI setup first and error help!")

# Session state
if 'current_step' not in st.session_state:
    st.session_state.current_step = 0

# Progress
total = len(setup_steps)
st.progress(st.session_state.current_step / total)
st.caption(f"Step {st.session_state.current_step + 1} of {total}")

# Current step
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

# Buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("✅ Done – Next Step"):
        if st.session_state.current_step < total - 1:
            st.session_state.current_step += 1
            st.rerun()
        else:
            st.balloons()
            st.success("All set! You're ready for the workshop 🎉")

with col2:
    if st.button("❓ Stuck? Show Help"):
        with st.expander("Common Errors & Fixes", expanded=True):
            for tip in step.get("troubleshooting", []):
                st.markdown(f"- {tip}")

# Back & Restart
if st.session_state.current_step > 0:
    if st.button("⬅️ Back"):
        st.session_state.current_step -= 1
        st.rerun()

st.sidebar.button("🔄 Restart", on_click=lambda: st.session_state.update(current_step=0))

st.markdown("---")
st.caption("Made for Luigi Solutions Workshop • Nick Wedra")