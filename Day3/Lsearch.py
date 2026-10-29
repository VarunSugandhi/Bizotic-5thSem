list = [1,7,9,6,8]
target = 9

def linear_search(list, target) :
    for ele in (list):
        if ele == target:
            print("Element found")
            return
    print("Not found")
    return 

linear_search(list,target)

