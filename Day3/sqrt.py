# Leetcode problem number 69


def sqrts(n) :
    low = 0
    high = n
    while low <= high :
        mid = (low + high) // 2
        if mid*mid == n :
            print("sqrt of ",n ,"is: ",mid)
            return
        elif mid*mid > n :
            high = mid - 1
        else :
            low = mid + 1
    print("sqrt not found")
    return

n = int(input("Enter element whise sqrt has to be found: "))
sqrts(n)