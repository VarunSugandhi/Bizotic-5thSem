def binary_Search(arr , target) :
    low = 0
    high = len(arr) - 1
    while low <= high :
        mid = (low + high) // 2
        if arr[mid] == target :
            print("Element found at index : " ,mid)
            return
        elif arr[mid] < target :
            low = mid + 1
        else :
            high = mid - 1
    print("Element not found")
    return

arr = [1,2,5,7,9,11,13]
target = 9
binary_Search(arr,target)