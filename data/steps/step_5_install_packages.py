# data/steps/step_5_install_packages.py

step = {
    "title": "Step 5: Install Streamlit & Pandas",
    "instructions": "With venv active, install the tools.",
    "command": "pip install streamlit pandas",
    "troubleshooting": [
        "pip not found? Reactivate venv.",
        "Slow/error? Run 'pip install --upgrade pip' first.",
        "Version issue? Python 3.14 is experimental – try 3.12 if problems."
    ]
}
