REQUEST_COUNTER = {}

MAX_REQUESTS = 5

def check_rate_limit(user_id):
    count = REQUEST_COUNTER.get(user_id, 0)

    if count >= MAX_REQUESTS:
        return False

    REQUEST_COUNTER[user_id] = count + 1

    return True