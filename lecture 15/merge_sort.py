
def mergeSort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left_half=mergeSort(arr[:mid])
    right_half=mergeSort(arr[mid:])
    return merge (left_half,right_half)
def merge(left,right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j+=1
    # Append any remaining elemnts from either list
    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr=[12,11,13,5,6,7]
print("given array is",arr)
arr1=mergeSort(arr)
print("sorted array is",arr1)