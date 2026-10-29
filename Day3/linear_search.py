def linear_search(list , target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1


list = [1,7,9,6,8]
target = int(input("Enter the element to be found in list: "))
index = linear_search(list,target)

if index == -1 :
    print("Element", target, " not found in list")
else :
    print("Element" , list[index] ,"found in list at index ",index)