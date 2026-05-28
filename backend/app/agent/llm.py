from groq import Groq
import os
from app.agent.prompts import SYSTEM_PROMPT

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL_NAME = "llama-3.3-70b-versatile"

def generate_refund_response(
    customer,
    order,
    approved,
    reason
):

    prompt = prompt = f"""
STRICT BACKEND POLICY DECISION:

Refund Approved:
{approved}

Official Reason:
{reason}

You MUST explain this decision professionally.
You are NOT allowed to change the decision.
"""

    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content":SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_tokens=200
    )

    return completion.choices[0].message.content