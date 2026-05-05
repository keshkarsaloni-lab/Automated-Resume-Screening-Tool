# 🔹 Calculate skill match score
def calculate_skill_score(resume_text, skills_list):
    matched = 0

    for skill in skills_list:
        if skill.lower() in resume_text:
            matched += 1

    return matched / len(skills_list)


# 🔹 Final scoring function
def calculate_final_score(similarity_score, skill_score):
    
    # Weightage
    similarity_weight = 0.7
    skill_weight = 0.3

    final_score = (similarity_score * similarity_weight) + (skill_score * skill_weight)

    return final_score