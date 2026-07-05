from state import AgentState

# Import Bhanu's function
from nodes.interview import generate_interview_questions


def interview_generator(state: AgentState):

    jd = state["jd_text"]

    # Take the first retrieved candidate
    resume = state["retrieved_candidates"][0]["resume"]

    questions = generate_interview_questions(
        jd,
        resume
    )

    state["response"] = questions

    return state