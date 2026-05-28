from pydantic import BaseModel

class ChatRequest(BaseModel):
    customer_id: str
    order_id: str

class RefundDecision(BaseModel):
    customer: str
    order_id: str
    approved: bool
    reason: str