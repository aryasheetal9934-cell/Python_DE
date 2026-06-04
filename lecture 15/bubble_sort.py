
def bubbleSort(arr): ##function to perform bubble sort on the given array
    n=len(arr)    ## get the length of the array
    for i in range(n):   ## Traverse through all array elements
        for j in range(0,n-i-1):   ## last i element are already in place so we can ignore them
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]  ## swapping the elements if they are int the wrong order

arr=[64,34,25,12,22,90]
bubbleSort(arr)
print(arr)