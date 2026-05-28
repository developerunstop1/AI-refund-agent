import json
from faker import Faker
import random

fake = Faker()

customers = []

for i in range(15):
    customers.append({
        "customer_id": f"CUST-{i+1}",
        "name": fake.name(),
        "email": fake.email(),
        "orders": [
            {
                "order_id": f"ORD-{i+1}",
                "item": fake.word(),
                "item_type": random.choice([
                    "electronics",
                    "clothing",
                    "gift_card"
                ]),
                "days_since_purchase": random.randint(1, 60),
                "price": random.randint(20, 500)
            }
        ]
    })

with open("crm_data.json", "w") as f:
    json.dump(customers, f, indent=2)

print("CRM data generated")