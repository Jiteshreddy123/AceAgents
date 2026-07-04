"""
parser.py
Purpose: Extract structured fields from raw resume text.
"""
def parse_resume(resume_text):
    # Default structure
    candidate_data = {
        "name": "Unknown",
        "experience": "Unknown",
        "skills": [],
        "raw_text": resume_text
    }
    
    # Simple extraction by reading line by line
    lines = resume_text.split('\n')
    for line in lines:
        if line.startswith("Name:"):
            candidate_data["name"] = line.replace("Name:", "").strip()
        elif line.startswith("Experience:"):
            candidate_data["experience"] = line.replace("Experience:", "").strip()
        elif line.startswith("Skills:"):
            skills_string = line.replace("Skills:", "").strip()
            candidate_data["skills"] = [skill.strip() for skill in skills_string.split()]
            
    return candidate_data