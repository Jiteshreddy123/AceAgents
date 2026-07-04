from state import AgentState 

def router(state: AgentState) -> AgentState:
    query = state["query"].lower()
    if any(word in query for word in [
    "count",
    "applicant",
    "applicants",
    "number",
    "total",
    "how many",
    "received",
    "applied"
    ]):
        state["intent"] = "count_applicants"   
    elif any(word in query for word in [
    "candidate",
    "candidates",
    "resume",
    "resumes",
    "top",
    "best",
    "match",
    "matching",
    "shortlist",
    "find",
    "search"
    ]):
        state["intent"] = "retrieve_candidates"
    elif any(word in query for word in [
    "rewrite",
    "improve",
    "modify",
    "enhance",
    "better",
    "optimize",
    "update",
    "edit",
    "refine",
    "rewrite jd"
    ]):
        state["intent"] = "rewrite_jd"
    elif any(word in query for word in [
    "interview",
    "questions",
    "question",
    "ask",
    "technical",
    "behavioral",
    "assessment",
    "screening"
    ]):
        state["intent"] = "generate_interview"
    elif any(word in query for word in [
    "salary",
    "pay",
    "compensation",
    "package",
    "ctc",
    "lpa",
    "wage",
    "market",
    "offer"
    ]):
        state["intent"] = "salary_lookup"
    else:
        state["intent"] = "unknown"

    print("Detected Intent:", state["intent"])
    return state

