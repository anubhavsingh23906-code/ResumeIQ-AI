ROLE_SKILLS = {

    "Machine Learning Engineer": [
        "python",
        "numpy",
        "pandas",
        "scikit-learn",
        "tensorflow",
        "pytorch",
        "sql",
        "docker",
        "git",
        "github",
        "streamlit",
        "fastapi"
    ],

    "Data Scientist": [
        "python",
        "numpy",
        "pandas",
        "sql",
        "machine learning",
        "matplotlib",
        "seaborn",
        "scikit-learn",
        "statistics"
    ],

    "Backend Developer": [
        "python",
        "java",
        "node.js",
        "express",
        "sql",
        "mongodb",
        "docker",
        "fastapi",
        "git"
    ],

    "Frontend Developer": [
        "html",
        "css",
        "javascript",
        "react",
        "git",
        "github"
    ]
}
SKILLS = []

for skills in ROLE_SKILLS.values():
    for skill in skills:
        if skill not in SKILLS:
            SKILLS.append(skill)

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return found_skills

def calculate_skill_score(found_skills):
    return min(len(found_skills) * 10, 100)
def get_missing_skills(found_skills, role):

    required = ROLE_SKILLS.get(role, [])

    missing = []

    for skill in required:
        if skill not in found_skills:
            missing.append(skill)

    return missing