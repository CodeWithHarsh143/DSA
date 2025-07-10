def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == "found":
            return mid
        elif result == "left":
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

def first_number(num, target):
    def condition(mid):
        if num[mid] == target:
            if mid > 0 and num[mid - 1] == target:
                return "left"
            return "found"
        elif num[mid] < target:
            return "right"
        else:
            return "left"
    return binary_search(0, len(num) - 1, condition)

def last_number(num, target):
    def condition(mid):
        if num[mid] == target:
            if mid < len(num) - 1 and num[mid + 1] == target:
                return "right"
            return "found"
        elif num[mid] < target:
            return "right"
        else:
            return "left"
    return binary_search(0, len(num) - 1, condition)

def first_and_last_number(num, target):
    first = first_number(num, target)
    last = last_number(num, target)
    return (first, last)

# Corrected Test Cases
test_cases = [
    {"input": {"num": [1, 2, 2, 2, 3, 4], "target": 2}, "expected": (1, 3)},
    {"input": {"num": [13, 11, 11, 8, 6, 5, 2], "target": 11}, "expected": (1, 2)},
    {"input": {"num": [13, 11, 8, 6, 5, 2, 13], "target": 13}, "expected": (0, 6)},
    {"input": {"num": [13, 11, 8, 6, 5, 2, 6], "target": 20}, "expected": (-1, -1)},
    {"input": {"num": [11, 11, 11, 11], "target": 4}, "expected": (-1, -1)},
    {"input": {"num": [], "target": 5}, "expected": (-1, -1)}
]

# Running Tests
for idx, test in enumerate(test_cases):
    result = first_and_last_number(**test["input"])
    print(f"Test case {idx + 1}:")
    if result == test["expected"]:
        print("✅ Passed")
    else:
        print("❌ Failed")
    print("Expected:", test["expected"])
    print("Output  :", result)
    print()
if __name__=="__main__":
    num=list(map(int,input().split(",")))
    target=int(input())
    print(first_and_last_number(num,target))
    
