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
       
    print("\n")
    print("=" * 60)
    print("🤖 ACEAGENTS RESPONSE")
    print("=" * 60)

    print(state["response"])

    print("=" * 60)

    return state