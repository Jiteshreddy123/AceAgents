from state import AgentState

def applicant_counter(state: AgentState) -> AgentState:
    
    candidates = state.get("retrieved_candidates", [])

    count = len(candidates)

    state["response"] = f"Total Applicants Found: {count}"

    return state