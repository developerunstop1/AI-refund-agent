import json

CRM_FILE = "app/db/crm_data.json"

def get_customer(customer_id: str):
    with open(CRM_FILE, "r") as f:
        data = json.load(f)

    for customer in data:
        if customer["customer_id"] == customer_id:
            return customer

    return None