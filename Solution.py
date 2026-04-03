def sort(width, height, length, mass):
    volume = width * height * length
    is_bulky = volume >= 1_000_000 or any(dim >= 150 for dim in (width, height, length))
    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return "REJECTED"
    if is_bulky or is_heavy:
        return "SPECIAL"
    return "STANDARD"


def run_tests():
    test_cases = [
        (10, 10, 10, 5,       "STANDARD"),
        (149, 1, 1, 1,        "STANDARD"),
        (10, 10, 9, 19,       "STANDARD"),
        (150, 1, 1, 1,        "SPECIAL"),
        (200, 1, 1, 5,        "SPECIAL"),
        (100, 100, 100, 5,    "SPECIAL"),
        (101, 100, 100, 5,    "SPECIAL"),
        (10, 10, 10, 20,      "SPECIAL"),
        (10, 10, 10, 50,      "SPECIAL"),
        (150, 1, 1, 20,       "REJECTED"),
        (200, 200, 200, 50,   "REJECTED"),
        (100, 100, 100, 20,   "REJECTED"),
        (149, 149, 149, 20,   "REJECTED"),
        (0, 0, 0, 0,          "STANDARD"),
        (150, 150, 150, 19,   "SPECIAL"),
    ]

    passed = 0
    failed = 0

    for width, height, length, mass, expected in test_cases:
        result = sort(width, height, length, mass)
        if result == expected:
            passed += 1
            print(f"PASS | {result}")
        else:
            failed += 1
            print(f"FAIL | Expected: {expected}, Got: {result}")

    print(f"\nResults: {passed} passed, {failed} failed out of {len(test_cases)} tests")


if __name__ == "__main__":
    run_tests()