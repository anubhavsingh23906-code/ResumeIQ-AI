ROADMAP = {

    "sql": [
        "Learn SQL Basics",
        "Practice SQL Queries",
        "Solve 20 SQL problems on LeetCode"
    ],

    "docker": [
        "Install Docker",
        "Learn Docker Images",
        "Containerize one Streamlit project"
    ],

    "tensorflow": [
        "Learn TensorFlow Basics",
        "Build a Neural Network",
        "Create an Image Classification Project"
    ],

    "github": [
        "Learn GitHub Workflow",
        "Push Projects",
        "Create a Professional README"
    ],

    "fastapi": [
        "Learn FastAPI",
        "Create REST APIs",
        "Deploy FastAPI Project"
    ],

    "streamlit": [
        "Learn Streamlit Widgets",
        "Build Dashboard",
        "Deploy on Streamlit Cloud"
    ]
}
def generate_roadmap(missing_skills):

    roadmap = []

    for skill in missing_skills:
        if skill in ROADMAP:
            roadmap.append({
                "skill": skill,
                "tasks": ROADMAP[skill]
            })

    return roadmap