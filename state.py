from typing import TypedDict, List, Optional


class AgentState(TypedDict):
    """
    This class stores everything the AI Agent knows
    while talking to the recruiter.
    """

    # Entire conversation history
    messages: List[str]

    # Current user question
    query: str

    # Router decision
    intent: str

    # Job Description text
    jd_text: str
 
    # Retrieved candidates from RAG
    retrieved_candidates: List[dict]

    # Salary information
    salary_data: str

    # Human confirmation
    confirmation: bool

    # Final response to display
    response: str









