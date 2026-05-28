from app.agent.graph import run_refund_agent

def test_agent_success():
    result = run_refund_agent(
        "CUST-1",
        "ORD-1"
    )

    assert "approved" in result


def test_agent_customer_not_found():
    result = run_refund_agent(
        "INVALID",
        "ORD-1"
    )

    assert result["status"] == "error"