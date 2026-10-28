def fibonacci(n):
    if n <= 1 :
        return n
    return fibonacci(n-1) + fibonacci(n-2)
num0 = 0
num1 = 1

"""
def fibonacci(n):
    if n <= 0:
        return num0
    elif n == 1:
        return num1
    else:
        for i in range(2, n + 1):
            next_num = num0 + num1
            num0 = num1
            num1 = next_num
        return num1
"""