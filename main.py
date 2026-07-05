from rag.vector_store import build_database
from graph import graph

build_database()

print("=" * 50)
print("AceAgents Recruitment AI")
print("=" * 50)

query = input("\nRecruiter Query: ")

jd_text = ""

if "rewrite" in query.lower() or "interview" in query.lower():
    print("\nPaste Job Description (Press Enter twice when finished):")

    lines = []

    while True:
        line = input()

        if line == "":
            break

        lines.append(line)

    jd_text = "\n".join(lines)

resume = ""

if "interview" in query.lower():

    print("\nPaste Candidate Resume (Press Enter twice when finished):")

    lines = []

    while True:
        line = input()

        if line == "":
            break

        lines.append(line)

    resume = "\n".join(lines)

state = {
    "messages": [],
    "query": query,
    "intent": "",
    "jd_text": jd_text,
    "retrieved_candidates": [{
        "resume": resume
    }] if resume else [],
    "salary_data": "",
    "confirmation": True,
    "response": "",
}

graph.invoke(state)