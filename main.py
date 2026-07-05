from rag.vector_store import build_database
from graph import graph

build_database()

print("=" * 50)
print("AceAgents Recruitment AI")
print("=" * 50)

query = input("\nRecruiter: ")

state = {
    "messages": [],
    "query": query,
    "intent": "",
    "jd_text": """Software Engineer

                Need java.
                Need SQL.
                Need teamwork.""",
    "retrieved_candidates": [{
                    "resume":
            """
            Python
            Flask
            Docker
            AWS
            """
                }],
    "salary_data": "",
    "confirmation": True,
    "response": "",
}

graph.invoke(state)