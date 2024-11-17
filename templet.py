import os
from pathlib import Path

project_name = "BioGenerator"



list_of_files = [
    "static/css/style.css",
    "static/js/main.js",
    "templates/index.html",
    "api/index.py",
    ".env",
    ".gitignore",
    "vercel.json",
    "requirements.txt",
]



for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
