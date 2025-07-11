test_cases = [
    {"input": {"num": [4,5,1,2,3]}, "expected": 2},
    {"input": {"num": []}, "expected": -1},
    {"input": {"num": [1,2,3,4,5], }, "expected": 0},
    
]
def locate_rotation(num):
    if not num:
        return -1
    position=0
    while position<len(num):
        if  position>0 and num[position-1]>num[position]:
            return position
        position+=1
    return 0
passed=0
failed=0
total=0
for idx,test in enumerate(test_cases):
    
    result=locate_rotation(**test['input'])
    total+=1
    if result==test['expected']:
        print("The test",idx+1,"PASSED")
        passed+=1
    else:
        print("The test",idx+1,"FAILED")
        print("Expected",test['expected'])
        print("output",result)
        failed+=1
        
print(f"TOTAL CASE:{total}, PASSED TESTS:{passed},FAILED TESTS:{failed}")




