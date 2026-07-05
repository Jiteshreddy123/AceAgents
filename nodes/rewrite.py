from tools.gemini_client import ask_gemini
from prompts.prompts import REWRITE_PROMPT


def rewrite_job_description(jd_text: str) -> str:
    """
    Rewrite a job description professionally.
    """

    prompt = REWRITE_PROMPT.format(
        jd=jd_text
    )

    response = ask_gemini(prompt)

    return response