# Count Sort

arr = [4,2,2,8,3,3,1]

def countSort(arr):
    if len(arr) == 0:
        return arr
    
    max_val = max(arr)
    count = [0] * (max_val+1)

    for num in arr:
        count[num] += 1
    
    result = []

    for i in range(len(count)) :
        for j in range(count[i]) :
            result.append(i)


    print(result)
countSort(arr)
