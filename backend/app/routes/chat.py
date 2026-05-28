from fastapi import APIRouter, HTTPException
from app.models.schemas import ChatRequest
from app.agent.graph import run_refund_agent
from app.guardrails.fraud_detection import detect_fraud
from app.guardrails.input_guard import (
    validate_customer_input
)

router = APIRouter()

@router.post("/chat")
def refund_chat(request: ChatRequest):

    valid, message = validate_customer_input(
        request.customer_id,
        request.order_id
    )

    if detect_fraud(message):
        raise HTTPException(
            status_code=403,
            detail="Suspicious activity detected"
        )

    if not valid:
        raise HTTPException(
            status_code=400,
            detail=message
        )

    result = run_refund_agent(
        request.customer_id,
        request.order_id
    )

    if result.get("status") == "error":
        raise HTTPException(
            status_code=404,
            detail=result["message"]
        )

    return result