sum = 0
l = [1,2,3,7,5]
target = 12
s = 0
for e in range(len(l)):
    sum += l[e]
    while sum > target :
        sum -= l[s]
        s += 1
    if (sum == target) :
        print(s+1 ," ", e+1)
        break