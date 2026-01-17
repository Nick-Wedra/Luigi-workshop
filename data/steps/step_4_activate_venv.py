# data/steps/step_4_activate_venv.py

step = {
    "title": "Step 4: Activate Virtual Environment",
    "instructions": "Activate the venv – look for (venv) in your prompt.",
    "command": None,
    "troubleshooting": [
        "Windows error: 'scripts disabled'? Run once: Set-ExecutionPolicy RemoteSigned -Scope CurrentUser",
        "No (venv) prompt? Wrong folder – cd back and retry.",
        "Mac: Use 'source venv/bin/activate'."
    ]
}
