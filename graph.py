from langgraph.graph import StateGraph, END 

from state import AgentState

from nodes.router import router
from nodes.applicant_counter import applicant_counter
from nodes.confirmation import confirmation
from nodes.response import response

workflow = StateGraph(AgentState)

# Add Nodes
workflow.add_node("router", router)
workflow.add_node("applicant_counter", applicant_counter)
workflow.add_node("confirmation", confirmation)
workflow.add_node("response", response)

# Entry Point
workflow.set_entry_point("router")


# Decide where router should go
def route(state: AgentState):
    intent = state["intent"]

    if intent == "count_applicants":
        return "applicant_counter"

    return "response"


workflow.add_conditional_edges(
    "router",
    route,
    {
        "applicant_counter": "applicant_counter",
        "response": "response",
    }
)

workflow.add_edge("applicant_counter", "confirmation")
workflow.add_edge("confirmation", "response")
workflow.add_edge("response", END)

graph = workflow.compile()