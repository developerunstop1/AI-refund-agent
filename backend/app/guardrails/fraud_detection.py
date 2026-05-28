SUSPICIOUS_KEYWORDS = [
    "chargeback",
    "lawsuit",
    "fake",
    "hack"
]

def detect_fraud(message: str):
    message = message.lower()

    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in message:
            return True

    return False