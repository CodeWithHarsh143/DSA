def printsum(n,sum):
    if n<1:
        print(sum)
        return
    printsum(n-1,sum+n)
def main():
    n=int(input())
    sum=0
    printsum(n,sum)
main()