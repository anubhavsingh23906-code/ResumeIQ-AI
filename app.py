import streamlit as st
from resume_parser import extract_text
from skills import (
    extract_skills,
    calculate_skill_score,
    get_missing_skills
)
from resources import LEARNING_RESOURCES
from roadmap import generate_roadmap
from job_match import calculate_job_match
st.title("ResumeIQ AI")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    text = extract_text(uploaded_file)

    st.subheader("Extracted Resume Text")
    st.text_area("Resume Content", text, height=300)

    skills = extract_skills(text)
    score = calculate_skill_score(skills)

    st.subheader("ATS Skill Score")
    st.progress(score / 100)

    st.metric("Score", f"{score}/100")

    st.subheader("Detected Skills")

    if skills:
        for skill in skills:
            st.success(skill)
    else:
        st.warning("No skills detected")

    # Career Goal
    role = st.selectbox(
        "Choose your career goal",
        [
            "Machine Learning Engineer",
            "Data Scientist",
            "Backend Developer",
            "Frontend Developer"
        ]
    )

    # Missing Skills
    missing = get_missing_skills(skills, role)

    st.subheader("Missing Skills")

    for skill in missing:
        st.error("❌ " + skill)
    # -----------------------------
    # Learning Resources
    # -----------------------------

    st.header("📚 Learn Missing Skills")

    for skill in missing:

        if skill in LEARNING_RESOURCES:

            resource = LEARNING_RESOURCES[skill]

            with st.expander(f"🚀 {skill.upper()}"):

                st.info(resource["description"])

                st.link_button(
                    "📖 Documentation",
                    resource["docs"]
                )

                st.link_button(
                    "🎥 Watch Tutorial",
                    resource["youtube"]
                )

    # -----------------------------
    # Personalized Learning Roadmap
    # -----------------------------

    roadmap = generate_roadmap(missing)

    st.header("🛣 Personalized Learning Roadmap")

    for item in roadmap:

        st.subheader(item["skill"].title())

        for task in item["tasks"]:
            st.write("✅", task)
st.header("💼 Job Description Matching")

job_description = st.text_area(
    "Paste Job Description Here"
)
if job_description:

    score, matched, missing_job = calculate_job_match(
        text,
        job_description
    )

    st.subheader("Job Match Score")

    st.progress(score / 100)

    st.metric("Match", f"{score}%")

    st.subheader("✅ Matching Skills")

    for skill in matched:
        st.success(skill)

    st.subheader("❌ Missing Skills")

    for skill in missing_job:
        st.error(skill)