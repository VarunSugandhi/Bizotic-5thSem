list = [1,2,3,0,4,1,6]
k = 3
s = 0 
l = len(list) - 1
max_sum = 0

while((s + k) <= len(list)) :
    total = 0
    for i in range(s, s + k):
        total += list[i]
    max_sum = max(max_sum, total)
    
    s += 1
print("The maximum sum of a subarray of length " + str(k) + " is:", max_sum)


