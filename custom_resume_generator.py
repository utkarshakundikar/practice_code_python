from docx import Document
from difflib import get_close_matches
import re

# Mapping of known skills to their categories
SKILL_CATEGORIES = {
    "Frontend": {"react.js", "redux", "bootstrap", "tailwind", "jquery", "html5", "css3", "typescript", "javascript"},
    "Backend": {"django", "flask", "node.js", "restful apis", "rest api"},
    "Database": {"mongodb", "postgresql", "mysql"},
    "Testing": {"cypress", "jest", "manual testing"},
    "Dev Tools": {"git", "jira", "vs code", "chrome devtools"},
    "Others": {"api", "ci/cd", "aws", "docker", "json", "csv", "cloud"},
}

def tailor_resume(jd_text: str):
    doc = Document(r"C:\Users\shukl\Downloads\utkarsha_resume.docx")
    print("📄 Resume loaded successfully!")
    jd_keywords = extract_keywords(jd_text)
    print("🔍 Extracted keywords from job description:", jd_keywords)
    for para in doc.paragraphs:
        line = para.text.strip()

        for category, skill_set in SKILL_CATEGORIES.items():
            if line.lower().startswith(f"● {category.lower()}"):
                updated_line = update_category_skills(line, jd_keywords, skill_set)
                para.text = updated_line

    doc.save(r"C:\Users\shukl\OneDrive\Desktop\resume_customized.docx")
    print("✅ Resume updated and saved successfully.")

def extract_keywords(jd_text):
    words = [word.strip('.,:;()').lower() for word in jd_text.split()]
    jd_keywords = set()
    for category_skills in SKILL_CATEGORIES.values():
        for skill in category_skills:
            if skill in jd_text.lower():
                jd_keywords.add(skill)
    return list(jd_keywords)

def update_category_skills(existing_line, jd_keywords, category_skills):
    # Extract category name and existing skills from the line
    match = re.match(r'●\s*(.+?):\s*(.*)', existing_line)
    if not match:
        return existing_line  # skip if format is unexpected

    category_name, skills_text = match.groups()
    existing_skills = {s.strip().lower() for s in skills_text.split(',')}
    updated_skills = set(existing_skills)

    for skill in jd_keywords:
        if skill in category_skills and not get_close_matches(skill, existing_skills, n=1, cutoff=0.85):
            updated_skills.add(skill)

    formatted_skills = ', '.join(sorted(s.capitalize() if not s.isupper() else s for s in updated_skills))
    return f"● {category_name}: {formatted_skills}"
