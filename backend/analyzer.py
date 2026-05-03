from langchain_core.prompts import ChatPromptTemplate
from backend.llm import get_llm

def analyze_lead(lead_text):
    
    llm = get_llm()

    prompt = ChatPromptTemplate.from_template("""

You are an AI sales assistant.

Analyze the lead and extract:

- intent (pricing, demo, support, other)
- urgency (low,, medium, high)
- sentiment (positive, neutral, negative)

Rules:
- Be strict
- Do not explain
- Return ONLY valid JSON.

Lead:
{lead}

Output format:
{{
    "intent" : "...",
    "urgency": "...",
    "sentiment": "..."                                            
}}

""")
    
    chain = prompt | llm

    response = chain.invoke({"lead": lead_text})

    return response.content