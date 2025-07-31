def rotate(arr,n,d):
    if d>len(arr):
        d=d%n
    elif d==len(arr):
        return arr
    temp=arr[:d]# new thing i learn today:)
    for i in range(d):
        temp[i]=arr[i]
    for i in range(d,n):
        arr[i-d]=arr[i]
    for i in range(n-d,n):
        arr[i]=temp[i-(n-d)]
    return print("Rotated arry:",arr)
def main():
    arr=list( map( int , input("Enter your arry:").split(",") ) )
    n=len(arr)
    d=int(input("Enter your rotation: "))
    rotate(arr,n,d)
    
main()