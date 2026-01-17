# data/steps/step_3_create_venv.py

step = {
    "title": "Step 3: Create Virtual Environment",
    "instructions": "Create a clean venv in your project folder.",
    "command": None,
    "troubleshooting": [
        "Permission denied? Run as admin (Windows) or sudo (Mac – rare).",
        "Already exists? Delete old 'venv' folder and retry.",
        "Module 'venv' not found? Python too old – reinstall 3.8+."
    ]
}
