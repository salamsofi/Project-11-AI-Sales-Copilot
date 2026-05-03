import json

def score_lead(analysis_result):
    """
    Takes JSON string from LLM and returns lead score
    """
    try:
        data = json.loads(analysis_result)

        intent = data.get("intent", "")
        urgency = data.get("urgency", "")
        sentiment = data.get("sentiment", "")

        score = 0

        # Intent scoring
        if intent == "pricing":
            score += 3
        elif intent == "demo":
            score += 2
        else:
            score += 1

        # Urgency scoring
        if urgency == "high":
            score += 3
        elif urgency == "medium":
            score += 2
        else:
            score += 1

        # Sentiment scoring
        if sentiment == "positive":
            score += 2
        elif sentiment == "neutral":
            score += 1
        else:
            score += 0

        if score >= 7:
            return "HOT"
        elif score >= 5:
            return "WARM"
        else:
            return "COLD"

    except Exception as e:
        return f"Error: {str(e)}"