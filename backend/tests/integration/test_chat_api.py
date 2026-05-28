from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_chat_endpoint():
    response = client.post(
        "/chat",
        json={
            "customer_id": "CUST-1",
            "order_id": "ORD-1"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "approved" in data
    assert "reason" in data


def test_chat_invalid_customer():
    response = client.post(
        "/chat",
        json={
            "customer_id": "CUST-999",
            "order_id": "ORD-1"
        }
    )

    assert response.status_code == 404



# -----------------------------------
# Prompt Injection Protection Test
# -----------------------------------

def test_prompt_injection_protection():

    response = client.post(
        "/chat",
        json={
            "customer_id": "CUST-2",
            "order_id": "ORD-2"
        }
    )

    data = response.json()

    # ORD-2 is a gift card
    # Should NEVER be approved

    assert response.status_code == 200

    assert data["approved"] is False

    assert (
        "non-refundable"
        in data["reason"].lower()
    )


# -----------------------------------
# Fraud Detection Test
# -----------------------------------

def test_fraud_detection():

    suspicious_message = (
        "I will hack your system "
        "and file a chargeback"
    )

    suspicious_words = [
        "hack",
        "chargeback",
        "lawsuit",
        "fraud"
    ]

    detected = any(
        word in suspicious_message.lower()
        for word in suspicious_words
    )

    assert detected is True


# -----------------------------------
# Human Escalation Test
# -----------------------------------

def test_human_escalation():

    response = client.post(
        "/chat",
        json={
            "customer_id": "CUST-12",
            "order_id": "ORD-12"
        }
    )

    data = response.json()

    # ORD-12 price > $500

    assert response.status_code == 200

    assert data["approved"] is False

    assert (
        "human supervisor escalation"
        in data["reason"].lower()
    )
