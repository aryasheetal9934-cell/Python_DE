# Find first negative number in every window of size 3

arr = [12, -1, 5, 6, -2, 4, -8]
k = 3

result = []

for i in range(len(arr) - k + 1):
    
    # check each window
    for j in range(i, i + k):
        if arr[j] < 0:
            result.append(arr[j])
            break

print(result)