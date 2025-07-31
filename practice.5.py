# rotate an arry by one place!!!
arr=list( map( int, input("Enter your arry: ").split(",") ) )
i=0
j=1
while j<len(arr):
    arr[i],arr[j]=arr[j],arr[i]
    i+=1
    j+=1
print(arr)



