from collections.abc import Container

def pytest_assertrepr_compare(op, left, right):
#     if isinstance(left, int) and isinstance(right, int ) and op == "==":
#         print(op, left, right)
#         return None
    if isinstance(left, object) and isinstance(right, Container ) and op == "not in":
        return [
            f"Prüfe ob {left} Teil der Liste ist.",
            f"Fehler: Element {left} gefunden, sollte aber nicht gefunden werden."
        ]
    if isinstance(left, object) and isinstance(right, Container ) and op == "in":
        return [
            f"Prüfe ob {left} Teil der Liste ist.",
            f"Fehler: Element {left} nicht gefunden, sollte aber gefunden werden."
        ]
    pass