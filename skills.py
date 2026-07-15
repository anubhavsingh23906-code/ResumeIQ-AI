SKILLS = [
    "python",
    "c++",
    "java",
    "javascript",
    "html",
    "css",
    "react",
    "node.js",
    "express",
    "sql",
    "mysql",
    "mongodb",
    "pandas",
    "numpy",
    "scikit-learn",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "streamlit",
    "git",
    "github",
    "docker",
    "fastapi"
]

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return found_skills


def calculate_skill_score(skills):
    return min(len(skills) * 10, 100)