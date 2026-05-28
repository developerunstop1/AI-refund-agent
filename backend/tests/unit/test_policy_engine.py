from app.agent.policy_engine import evaluate_refund

def test_refund_approved():
    order = {
        "days_since_purchase": 10,
        "item_type": "electronics",
        "price": 100
    }

    approved, reason = evaluate_refund(order)

    assert approved is True
    assert "approved" in reason.lower()


def test_refund_denied_time_limit():
    order = {
        "days_since_purchase": 45,
        "item_type": "electronics",
        "price": 100
    }

    approved, reason = evaluate_refund(order)

    assert approved is False
    assert "30-day" in reason


def test_refund_denied_non_refundable():
    order = {
        "days_since_purchase": 5,
        "item_type": "gift_card",
        "price": 100
    }

    approved, reason = evaluate_refund(order)

    assert approved is False