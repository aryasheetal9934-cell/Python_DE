def maxsubarray(arr,k):
    n=len(arr)
    if n<k:
        return -1
    ws=sum(arr[:k])
    maxsum=ws

    for i in range(k,n):
        ws += arr[i]-arr[i-k]
        maxsum=max(maxsum,ws)
    return maxsum
if __name__ == "__main__":
    arr=[5,2,-1,0,3]
    k=3
    print(maxsubarray(arr,k))