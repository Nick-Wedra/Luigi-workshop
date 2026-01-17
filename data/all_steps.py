# data/all_steps.py - Loads every individual step stub

from .steps.step_0_chatgpt import step as step_0
from .steps.step_1_vscode import step as step_1
from .steps.step_2_python import step as step_2
from .steps.step_3_create_venv import step as step_3
from .steps.step_4_activate_venv import step as step_4
from .steps.step_5_install_packages import step as step_5
from .steps.step_6_test import step as step_6

setup_steps = [
    step_0,
    step_1,
    step_2,
    step_3,
    step_4,
    step_5,
    step_6
]
