from state import AgentState
from tools.tavily_tool import get_salary_information

def salary_lookup(state: AgentState):

    state["response"] = get_salary_information(state["query"])

    return state