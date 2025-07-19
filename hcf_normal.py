def printHCF(a,b):
    for i in range(min(a,b),0,-1):
        if a%i==0 and b%i==0:
            return i
    return 1
def main():
    a,b=map(int,input().split())
    print(printHCF(a,b))
if __name__=="__main__":
    main()