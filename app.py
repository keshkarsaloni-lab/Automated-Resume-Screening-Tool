import streamlit as st
import os

from src.cleaner import clean_text
from src.matcher import match_resume_to_jd
from src.scorer import calculate_skill_score, calculate_final_score
from src.utils import load_skills

st.set_page_config(page_title="Resume Screening Tool")

st.title("📄 Automated Resume Screening Tool")

# Upload Resume
uploaded_file = st.file_uploader("Upload Resume (TXT only for now)", type=["txt"])

# Job Description Input
jd_input = st.text_area("Enter Job Description")

# Load skills
skills_path = os.path.join("data", "job_description", "skills.txt")
skills = load_skills(skills_path)

if st.button("Analyze Resume"):
    if uploaded_file and jd_input:
        resume_text = uploaded_file.read().decode("utf-8")

        # Clean text
        clean_resume = clean_text(resume_text)
        clean_jd = clean_text(jd_input)

        # Scores
        similarity = match_resume_to_jd(clean_resume, clean_jd)
        skill_score = calculate_skill_score(clean_resume, skills)
        final_score = calculate_final_score(similarity, skill_score)

        # Display Results
        st.subheader("📊 Results")

        st.write(f"**Similarity Score:** {round(similarity * 100, 2)}%")
        st.write(f"**Skill Match Score:** {round(skill_score * 100, 2)}%")
        st.write(f"**Final Score:** {round(final_score * 100, 2)}%")

        if final_score >= 0.5:
            st.success("✅ SHORTLISTED")
        else:
            st.error("❌ REJECTED")

    else:
        st.warning("Please upload resume and enter job description")