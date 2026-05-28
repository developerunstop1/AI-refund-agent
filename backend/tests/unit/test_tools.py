from app.agent.tools import get_customer

def test_get_existing_customer():
    customer = get_customer("CUST-1")

    assert customer is not None
    assert customer["customer_id"] == "CUST-1"


def test_get_invalid_customer():
    customer = get_customer("INVALID")

    assert customer is None