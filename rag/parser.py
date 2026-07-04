"""
parser.py
Purpose: Extract structured fields from raw resume text.
"""
import re

def parse_resume(resume_text):
    candidate_data = {
        "name": "Unknown",
        "experience": "Unknown",
        "skills": [],
        "raw_text": resume_text
    }
    
    # 1. Extract Name
    name_match = re.search(r"Name:\s*(.+)", resume_text)
    if name_match:
        candidate_data["name"] = name_match.group(1).strip()
        
    # 2. Extract Experience (smart enough to check the next line)
    exp_match = re.search(r"Experience:\s*\n*([^\n]+)", resume_text)
    if exp_match:
        candidate_data["experience"] = exp_match.group(1).strip()
        
    # 3. Extract Skills (grabs all lines until it hits "Projects:")
    skills_match = re.search(r"Skills:\s*\n(.*?)(?=\n\n|\nProjects:|$)", resume_text, re.DOTALL)
    if skills_match:
        skills_raw = skills_match.group(1)
        # Split by newlines and clean up empty spaces
        candidate_data["skills"] = [skill.strip() for skill in skills_raw.split('\n') if skill.strip()]
        
    return candidate_data