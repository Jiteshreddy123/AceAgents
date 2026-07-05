from state import AgentState
from rag.retriever import search_candidates


def candidate_retriever(state: AgentState):

    print("Candidate Retriever Node Running...")

    results = search_candidates(state["query"])

    state["retrieved_candidates"] = results

    if not results:
        state["response"] = "❌ No matching candidates found."
        return state

    response = "\n🏆 TOP MATCHING CANDIDATES\n"
    response += "=" * 45 + "\n\n"

    for i, candidate in enumerate(results, start=1):

        response += (
            f"{i}. 👤 Name       : {candidate['name']}\n"
            f"   🎯 Match      : {candidate['match_score']}\n"
            f"   💼 Experience : {candidate['experience']}\n"
            f"   🛠 Skills     : {', '.join(candidate['skills'])}\n"
            f"   🆔 Candidate  : {candidate['candidate_id']}\n"
            "\n---------------------------------------------\n\n"
        )

    state["response"] = response

    return state