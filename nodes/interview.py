from tools.gemini_client import ask_gemini
from prompts.prompts import INTERVIEW_PROMPT


def generate_interview_questions(jd_text, resume_text):

    prompt = INTERVIEW_PROMPT.format(
        jd=jd_text,
        resume=resume_text,
    )
    response = ask_gemini(prompt)

    return response