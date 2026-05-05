from src.parser import extract_all_resumes
from src.cleaner import clean_text
from src.matcher import match_resume_to_jd
from src.scorer import calculate_skill_score, calculate_final_score
from src.utils import read_file, load_skills
import os

# 🔹 Paths
resume_folder = os.path.join("data", "resumes")
jd_path = os.path.join("data", "job_description", "jd.txt")
skills_path = os.path.join("data", "job_description", "skills.txt")

# 🔹 Load JD
with open(jd_path, "r", encoding="utf-8") as file:
    jd_text = file.read()

jd_cleaned = clean_text(jd_text)

# 🔹 Load Skills
with open(skills_path, "r", encoding="utf-8") as file:
    skills = [line.strip().lower() for line in file.readlines()]

# 🔹 Extract resumes
resumes = extract_all_resumes(resume_folder)

print("\nTotal resumes found:", len(resumes))

# 🔹 Store results
results = []

for name, text in resumes.items():
    cleaned_resume = clean_text(text)

    similarity = match_resume_to_jd(cleaned_resume, jd_cleaned)
    skill_score = calculate_skill_score(cleaned_resume, skills)
    final_score = calculate_final_score(similarity, skill_score)

    results.append({
        "name": name,
        "similarity": similarity,
        "skill_score": skill_score,
        "final_score": final_score
    })

# 🔹 Sort by final score (descending)
results = sorted(results, key=lambda x: x["final_score"], reverse=True)

# 🔹 Shortlisting threshold
threshold = 0.5  # 50%

# 🔹 Print ranked results
print("\n\n🏆 RANKED CANDIDATES")

for i, res in enumerate(results, start=1):
    status = "SHORTLISTED ✅" if res["final_score"] >= threshold else "REJECTED ❌"

    print("\n" + "="*50)
    print(f"Rank: {i}")
    print(f"Resume: {res['name']}")
    print(f"Final Score: {round(res['final_score'] * 100, 2)}%")
    print(f"Status: {status}")

    import pandas as pd

# 🔹 Convert results to DataFrame
df = pd.DataFrame(results)

# 🔹 Convert scores to percentage
df["similarity"] = df["similarity"] * 100
df["skill_score"] = df["skill_score"] * 100
df["final_score"] = df["final_score"] * 100

# 🔹 Add Status column
df["status"] = df["final_score"].apply(lambda x: "SHORTLISTED" if x >= 50 else "REJECTED")

# 🔹 Save to CSV
output_path = os.path.join("output", "results.csv")
df.to_csv(output_path, index=False)

print("\n📁 Report saved at:", output_path)