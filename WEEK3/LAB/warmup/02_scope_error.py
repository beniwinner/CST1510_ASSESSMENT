def check(value, limit):
    """Return the status based on the value and limit."""
    status = "OVER LIMIT" if value > limit else "OK"
    return status

status = check(87, 100)

print(status)