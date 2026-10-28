list = [1,2,3,0,4,1,6]
k = 3
sum = 0
max_sum = 0

for i in range(0,k):
    sum += list[i]

max_sum = sum

for i in range(k, len(list)):
    sum += list[i] - list[i-k]
    max_sum = max(max_sum, sum)

print("The maximum sum of a subarray of length " + str(k) + " is:", max_sum)