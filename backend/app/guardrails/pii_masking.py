import re

def mask_email(text: str):
    return re.sub(
        r'[\w\.-]+@[\w\.-]+',
        '[EMAIL_MASKED]',
        text
    )