from app.agent.tools import get_customer
from app.agent.policy_engine import evaluate_refund
from app.agent.llm import generate_refund_response

def run_refund_agent(customer_id, order_id):

    customer = get_customer(customer_id)

    if not customer:
        return {
            "status": "error",
            "message": "Customer not found"
        }

    order = next(
        (
            o for o in customer["orders"]
            if o["order_id"] == order_id
        ),
        None
    )

    if not order:
        return {
            "status": "error",
            "message": "Order not found"
        }

    approved, reason = evaluate_refund(order)

    ai_response = generate_refund_response(
        customer,
        order,
        approved,
        reason
    )

    return {
        "customer": customer["name"],
        "order_id": order["order_id"],
        "approved": approved,
        "reason": reason,
        "ai_response": ai_response
    }