from state import AgentState

def confirmation(state: AgentState) -> AgentState:
    if state["confirmation"]:
        state["response"] += "\n\nConfirmation received."

    else:
        state["response"] += "\n\nWaiting for recruiter confirmation."

    return state