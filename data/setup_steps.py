# data/setup_steps.py - All setup steps in one file (your "stubs" collection)

setup_steps = [
    {
        "title": "Step 0: Set Up ChatGPT (Recommended First)",
        "instructions": "Start with ChatGPT – your AI coding buddy!",
        "link": "https://chatgpt.com",
        "command": None,
        "troubleshooting": [
            "Can't access? Incognito or VPN.",
            "Prompt example: 'Explain Python setup for beginners'",
            "Error? Paste into ChatGPT: 'Fix this: [error]'"
        ]
    },
    {
        "title": "Step 1: Install VS Code",
        "instructions": "Download VS Code – our editor.",
        "link": "https://code.visualstudio.com/download",
        "command": None,
        "troubleshooting": [
            "Already have it? Skip.",
            "Download stuck? Use link or another browser.",
            "Installer fails? Run as admin (Windows)."
        ]
    },
    {
        "title": "Step 2: Install Python 3.10+",
        "instructions": "Download Python. Windows: Check 'Add to PATH'.",
        "link": "https://www.python.org/downloads/",
        "command": None,
        "troubleshooting": [
            "'python' not found? Reinstall with PATH checked.",
            "Store opens? Turn off aliases in Settings > Apps.",
            "Mac: Use 'python3'."
        ]
    },
    {
        "title": "Step 3: Create Virtual Environment",
        "instructions": "Run this in terminal:",
        "command": "python -m venv venv",
        "troubleshooting": [
            "Permission denied? Run as admin.",
            "Already exists? Delete old venv.",
            "Module not found? Reinstall Python 3.8+."
        ]
    },
    {
        "title": "Step 4: Activate Virtual Environment",
        "instructions": "Activate – look for (venv) in prompt:",
        "command": "venv\\Scripts\\activate",
        "troubleshooting": [
            "Scripts disabled? Run: Set-ExecutionPolicy RemoteSigned -Scope CurrentUser",
            "No (venv)? Wrong folder.",
            "Mac: source venv/bin/activate"
        ]
    },
    {
        "title": "Step 5: Install Packages",
        "instructions": "With (venv) active, install:",
        "command": "pip install streamlit pandas",
        "troubleshooting": [
            "pip not found? Reactivate venv.",
            "Slow? pip install --upgrade pip first."
        ]
    },
    {
        "title": "Step 6: Test Setup",
        "instructions": "Run this – browser should open demo:",
        "command": "streamlit hello",
        "troubleshooting": [
            "Not found? Venv not active.",
            "No browser? Go to http://localhost:8501"
        ]
    }
]