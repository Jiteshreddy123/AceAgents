"""
loader.py

Purpose:
--------
Load the Job Description and all resume text files
from the data folder.

This module DOES NOT perform any AI operations.
It only reads files from disk.
"""

from pathlib import Path


# ----------------------------------------------------
# Folder Paths
# ----------------------------------------------------

# AceAgents/
BASE_DIR = Path(__file__).resolve().parent.parent

# AceAgents/data/resumes
RESUME_DIR = BASE_DIR / "data" / "resumes"

# AceAgents/data/jd
JD_DIR = BASE_DIR / "data" / "jd"


# ----------------------------------------------------
# Load Job Description
# ----------------------------------------------------

def load_job_description(filename: str = "software_engineer.txt") -> str:
    """
    Load the job description file.

    Returns
    -------
    str
        Complete JD text.
    """

    jd_path = JD_DIR / filename

    if not jd_path.exists():
        raise FileNotFoundError(
            f"Job Description not found:\n{jd_path}"
        )

    return jd_path.read_text(encoding="utf-8")


# ----------------------------------------------------
# Load All Resumes
# ----------------------------------------------------

def load_resumes():
    """
    Reads every resume inside data/resumes.

    Returns
    -------
    list

    Example

    [
        {
            "id":"resume_01",
            "filename":"resume_01.txt",
            "text":"...."
        },

        {
            "id":"resume_02",
            "filename":"resume_02.txt",
            "text":"...."
        }
    ]
    """

    resumes = []

    if not RESUME_DIR.exists():
        raise FileNotFoundError(
            f"Resume directory not found:\n{RESUME_DIR}"
        )

    resume_files = sorted(
        RESUME_DIR.glob("*.txt")
    )

    if len(resume_files) == 0:
        raise ValueError(
            "No resumes found inside data/resumes/"
        )

    for file in resume_files:

        resume = {
            "id": file.stem,
            "filename": file.name,
            "text": file.read_text(
                encoding="utf-8"
            )
        }

        resumes.append(resume)

    return resumes


# ----------------------------------------------------
# Quick Test
# ----------------------------------------------------
if __name__ == "__main__":

    jd = load_job_description()
    resumes = load_resumes()

    print("=" * 60)
    print(f"Total Resumes Loaded: {len(resumes)}")
    print("=" * 60)

    print("\nResume Files Loaded:\n")

    for resume in resumes:
        print(f"✅ {resume['filename']}")

    print(len(resumes))