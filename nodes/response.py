from state import AgentState

def response(state: AgentState) -> AgentState:
    if not state["response"]:
        state["response"] = (
            "Sorry, I couldn't understand your request.\n"
            "Try:\n"
            "- Count applicants\n"
            "- Show top candidates\n"
            "- Rewrite JD\n"
            "- Salary lookup"
        )

    print("\n===== FINAL RESPONSE =====")
    print(state["response"])
    print("==========================")

    return state