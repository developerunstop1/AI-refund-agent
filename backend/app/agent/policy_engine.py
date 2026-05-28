POLICY_RULES = {
    "refund_days_limit": 30,

    "non_refundable_items": [
        "gift_card",
        "downloadable_software",
        "final_sale",
        "digital_subscription",
        "customized_product"
    ],

    "human_escalation_amount": 500
}


def evaluate_refund(order):

    if order["days_since_purchase"] > 30:
        return (
            False,
            "Refund denied: exceeded 30-day limit"
        )

    if order["item_type"] in POLICY_RULES[
        "non_refundable_items"
    ]:
        return (
            False,
            f"Refund denied: {order['item_type']} items are non-refundable"
        )

    if order["price"] > POLICY_RULES[
        "human_escalation_amount"
    ]:
        return (
            False,
            "Refund requires human supervisor escalation"
        )

    return (
        True,
        "Refund approved under company policy"
    )