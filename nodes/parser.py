import re
from pathlib import Path
from pydantic import BaseModel
from typing import List


# -----------------------------
# Pydantic Model
# -----------------------------
class JobDescription(BaseModel):
    job_title: str
    location: str
    company: str
    about: str
    role_description: str
    experience: str
    skills: List[str]


# -----------------------------
# Read JD File
# -----------------------------
def load_jd(file_path: str):

    path = Path(file_path)

    with open(path, "r", encoding="utf-8") as file:
        return file.read()


# -----------------------------
# Parse JD
# -----------------------------
def parse_jd(text: str):

    job_title = re.search(r"Job Title:\s*(.*)", text)
    location = re.search(r"Location:\s*(.*)", text)
    company = re.search(r"Company:\s*(.*)", text)

    about = re.search(
        r"About Us:\s*(.*?)Your Role:",
        text,
        re.DOTALL,
    )

    role = re.search(
        r"Your Role:\s*(.*?)Requirements",
        text,
        re.DOTALL,
    )

    experience = re.search(
        r"Requirements & Experience:(.*?)Technical Skills Required:",
        text,
        re.DOTALL,
    )

    skills_section = re.search(
        r"Technical Skills Required:(.*)",
        text,
        re.DOTALL,
    )

    skills = []

    if skills_section:

        section = skills_section.group(1)

        skills = re.findall(r":\s*(.*)", section)

        final_skills = []

        for line in skills:

            parts = line.split(",")

            for p in parts:

                final_skills.append(
                    p.strip()
                )

        skills = final_skills

    jd = JobDescription(

        job_title=job_title.group(1).strip(),

        location=location.group(1).strip(),

        company=company.group(1).strip(),

        about=about.group(1).strip(),

        role_description=role.group(1).strip(),

        experience=experience.group(1).strip(),

        skills=skills,

    )

    return jd