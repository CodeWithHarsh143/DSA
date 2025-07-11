def locate_rotations(num):
    if not num:
        return -1
    lo,hi=0,len(num)-1
    while lo<=hi:
        mid=(lo+hi)//2
        if mid>0 and num[mid]<num[mid-1]:
            return mid
        elif num[mid]>num[-1]:
            lo=mid+1
        else:
            hi=mid-1
    return 0
test_cases = [
    {"input": {"num": [4,5,1,2,3]}, "expected": 2},
    {"input": {"num": []}, "expected": -1},
    {"input": {"num": [1,2,3,4,5], }, "expected": 0},
    
]
passed=0
failed=0
total=0
for idx,test in enumerate(test_cases):
    
    result=locate_rotations(**test['input'])
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


        