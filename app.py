import streamlit as st
from resume_parser import extract_text
from skills import extract_skills
from skills import extract_skills, calculate_skill_score
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