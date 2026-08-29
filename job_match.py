from skills import extract_skills

def calculate_job_match(resume_text, job_description):

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    matched = []

    missing = []

    for skill in job_skills:
        if skill in resume_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    if len(job_skills) == 0:
        score = 0
    else:
        score = int((len(matched) / len(job_skills)) * 100)

    return score, matched, missing