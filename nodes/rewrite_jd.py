from state import AgentState

from nodes.rewrite import rewrite_job_description


def rewrite_jd(state: AgentState):

    jd = state["jd_text"]

    improved = rewrite_job_description(jd)

    state["response"] = improved

    return state