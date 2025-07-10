
def test_locate_cards(cards, query, mid):
    mid_number = cards[mid]
    if mid_number == query:
        if mid - 1 >= 0 and cards[mid - 1] == query:
            return -1
        else:
            return 0
    elif mid_number < query:
        return -1
    else:
        return 1


def locate_cards(cards, query):
    lo, hi = 0, len(cards) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        result = test_locate_cards(cards, query, mid)
        if result == 0:
            return mid
        elif result == -1:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


# ✅ Test cases list
test_cases = [
    {"input": {"cards": [13, 11, 8, 6, 5, 2], "query": 8}, "expected": 2},
    {"input": {"cards": [13, 11, 11, 8, 6, 5, 2], "query": 11}, "expected": 1},
    {"input": {"cards": [13, 11, 8, 6, 5, 2], "query": 13}, "expected": 0},
    {"input": {"cards": [13, 11, 8, 6, 5, 2], "query": 2}, "expected": 5},
    {"input": {"cards": [13, 11, 8, 6, 5, 2], "query": 4}, "expected": -1},
    {"input": {"cards": [], "query": 5}, "expected": -1},
    {"input": {"cards": [5], "query": 5}, "expected": 0},
    {"input": {"cards": [5], "query": 3}, "expected": -1},
]

# ✅ Running test cases
for idx, test in enumerate(test_cases):
    result = locate_cards(**test["input"])
    if result == test["expected"]:
        print(f"Test case {idx+1}: ✅ Passed")
    else:
        print(f"Test case {idx+1}: ❌ Failed (Expected {test['expected']}, Got {result})")

if __name__ == "__main__": 
    cards = list(map(int, input("Enter your cards (space-separated): ").split()))
    query = int(input("Enter your query: "))
    result = locate_cards(cards, query)
    print("Result:", result)
