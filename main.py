print("=" * 50)
print("AceAgents Recruitment AI")
print("=" * 50)

query = input("\nRecruiter: ")

state = {
    "messages": [],
    "query": query,
    "intent": "",
    "jd_text": "",
    "retrieved_candidates": [],
    "salary_data": "",
    "confirmation": True,
    "response": "",
}

graph.invoke(state)