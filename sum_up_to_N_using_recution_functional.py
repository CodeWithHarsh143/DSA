def printSum(n):
    if n==0:
        return 0
    return n + printSum(n-1)
def main():
    n=int(input())
    print(printSum(n))
main()