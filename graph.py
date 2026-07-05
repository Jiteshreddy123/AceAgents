from nodes.candidate_retriever import candidate_retriever
from langgraph.graph import StateGraph, END  

from state import AgentState

from nodes.router import router
from nodes.applicant_counter import applicant_counter
from nodes.confirmation import confirmation
from nodes.response import response
from nodes.salary_lookup import salary_lookup
from nodes.rewrite_jd import rewrite_jd
from nodes.interview_generator import interview_generator

workflow = StateGraph(AgentState)

# Add Nodes
workflow.add_node("router", router)
workflow.add_node("applicant_counter", applicant_counter)
workflow.add_node("confirmation", confirmation)
workflow.add_node("response", response)
workflow.add_node("candidate_retriever",candidate_retriever)
workflow.add_node("salary_lookup",salary_lookup)
workflow.add_node("rewrite_jd",rewrite_jd)
workflow.add_node("interview_generator",interview_generator)

# Entry Point
workflow.set_entry_point("router")


# Decide where router should go
def route(state: AgentState):
    intent = state["intent"]

    if intent == "count_applicants":
        return "applicant_counter"
    elif intent == "retrieve_candidates":
        return "candidate_retriever"
    elif intent == "salary_lookup":
        return "salary_lookup"    
    elif intent == "rewrite_jd":
        return "rewrite_jd"
    elif intent == "generate_interview":
        return "interview_generator"
    else:
        state["response"] = "I'm sorry, I didn't understand your request. Please try again."
        return "response"
    


workflow.add_conditional_edges(
    "router",
    route,
    {
        "applicant_counter": "applicant_counter",
        "candidate_retriever": "candidate_retriever",
        "salary_lookup": "salary_lookup",
        "rewrite_jd": "rewrite_jd",
        "interview_generator": "interview_generator",
        "response": "response",
    }
)

workflow.add_edge("applicant_counter", "confirmation")
workflow.add_edge("confirmation", "response")
workflow.add_edge("candidate_retriever", "response")
workflow.add_edge("salary_lookup","response")
workflow.add_edge("rewrite_jd","response")
workflow.add_edge("interview_generator","response")
workflow.add_edge("response", END)

graph = workflow.compile()