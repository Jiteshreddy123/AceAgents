# ============================
# Rewrite Job Description
# ============================

REWRITE_PROMPT = """
You are an expert HR recruiter.

Rewrite the following Job Description professionally.

Instructions:
- Keep ALL technical requirements.
- Improve grammar.
- Make it attractive.
- Make it concise.
- Return ONLY the rewritten job description.

Job Description:

{jd}
"""

# ============================
# Interview Questions
# ============================

INTERVIEW_PROMPT = """
You are a Senior Technical Interviewer.

Given the Job Description and Candidate Resume,

Generate exactly 10 interview questions.

Requirements:

- Questions should test technical skills.
- Questions should match the candidate's experience.
- Questions should relate to the job description.
- Number each question.

Job Description:

{jd}

Candidate Resume:

{resume}
"""

# ============================
# Candidate Recommendation
# (Bonus Feature)
# ============================

RECOMMEND_PROMPT = """
You are an HR Hiring Manager.

Given:

Job Description

Candidate Resume

Provide

1. Strengths

2. Weaknesses

3. Missing Skills

4. Recommendation

Return format:

Strengths:

Weaknesses:

Missing Skills:

Recommendation:
Hire / Interview / Reject

Reason:
"""