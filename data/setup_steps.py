# data/setup_steps.py - All steps including AI/ChatGPT first + troubleshooting

setup_steps = [
    {
        "title": "Step 0: Set Up ChatGPT (Highly Recommended First!)",
        "instructions": "Since many participants are comfortable with AI, start with ChatGPT as your personal coding assistant!",
        "link": "https://chatgpt.com",
        "command": None,
        "troubleshooting": [
            "Can't access the site? Try incognito mode, different browser, or a VPN.",
            "First time? Just log in with Google/email, then type a prompt like:",
            "   'Explain how to install Python and create a virtual environment for beginners – step by step'",
            "Error messages? Copy-paste them directly into ChatGPT with context – it usually explains perfectly!"
        ]
    },
    {
        "title": "Step 1: Install VS Code",
        "instructions": "Download and install VS Code – the main editor we'll use.",
        "link": "https://code.visualstudio.com/download",
        "command": None,
        "troubleshooting": [
            "Already installed? Just open it and skip this step.",
            "Download stuck? Use the direct link above or try another browser.",
            "Installer fails? Right-click → Run as administrator (Windows) or check permissions (Mac)."
        ]
    },
    {
        "title": "Step 2: Install Python 3.10+",
        "instructions": "Download Python from the official site. **Windows users:** Check 'Add Python to PATH' during installation!",
        "link": "https://www.python.org/downloads/",
        "command": None,
        "troubleshooting": [
            "Command 'python' not found? Reinstall and make sure 'Add to PATH' is checked, then restart terminal.",
            "Mac users: Use 'python3' instead of 'python' in commands.",
            "Microsoft Store opens instead? Go to Settings → Apps → App execution aliases → turn off python.exe and python3.exe.",
            "Wrong version shown? Uninstall old Python versions first."
        ]
    },
    {
        "title": "Step 3: Create Virtual Environment",
        "instructions": "Create a clean virtual environment in your project folder.",
        "command": None,
        "troubleshooting": [
            "Permission denied? Run PowerShell as administrator (Windows) or use sudo (Mac – rare).",
            "Folder already exists? Delete the old 'venv' folder and try again.",
            "Module 'venv' not found? Your Python installation is too old – reinstall Python 3.8 or newer."
        ]
    },
    {
        "title": "Step 4: Activate Virtual Environment",
        "instructions": "Activate the venv – you should see (venv) appear in your prompt.",
        "command": None,
        "troubleshooting": [
            "Windows PowerShell error: 'cannot load because running scripts is disabled'? Run this one-time command: Set-ExecutionPolicy RemoteSigned -Scope CurrentUser",
            "No (venv) prompt after running? Make sure you're in the correct project folder with the venv inside.",
            "Mac/Linux: Use 'source venv/bin/activate' instead of the Windows version."
        ]
    },
    {
        "title": "Step 5: Install Required Packages",
        "instructions": "With (venv) active, install Streamlit and Pandas.",
        "command": "pip install streamlit pandas",
        "troubleshooting": [
            "pip not recognized? Make sure venv is active (look for (venv) in prompt).",
            "Slow or network error? Try: pip install --upgrade pip then retry the install.",
            "Version conflicts? If using Python 3.14, it may be experimental – consider 3.12 if issues persist."
        ]
    },
    {
        "title": "Step 6: Test Your Setup",
        "instructions": "Run this command – a browser window should open with the Streamlit demo.",
        "command": "streamlit hello",
        "troubleshooting": [
            "Streamlit command not found? Venv not active – deactivate then reactivate.",
            "Browser doesn't open automatically? Manually visit http://localhost:8501 in your browser.",
            "Port already in use? Close other apps or try: streamlit hello --server.port 8502"
        ]
    }
]