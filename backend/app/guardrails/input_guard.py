import re

def validate_customer_input(customer_id, order_id):
    customer_pattern = r"^CUST-\d+$"
    order_pattern = r"^ORD-\d+$"

    if not re.match(customer_pattern, customer_id):
        return False, "Invalid customer ID format"

    if not re.match(order_pattern, order_id):
        return False, "Invalid order ID format"

    return True, "Valid input"