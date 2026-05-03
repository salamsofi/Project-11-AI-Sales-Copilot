from backend.analyzer import analyze_lead
from backend.scorer import score_lead
from backend.rag import rag_response

def run_agents(user_input):
    """
    Central controller for all agents.
    """

    # Agent 1 --> Analyzer
    analysis = analyze_lead(user_input)

    # Agent 2 --> Lead score
    score = score_lead(analysis)

    # Agent 3 --> RAG
    response = rag_response(user_input)

    # Agent 4 --> Action decision
    action =  decide_action(score)

    return {
        "analysis": analysis,
        "score": score,
        "response": response,
        "action": action
    }


def decide_action(score):
    """
    Action agent logic
    """

    if score == "HOT":
        return "Schedule Call Immediately"
    elif score == "WARM":
        return "Send Follow-up Email"
    else:
        return "Add to Nurture Campaign"