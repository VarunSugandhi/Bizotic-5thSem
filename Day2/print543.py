def print_num(n):
    if n > 0:
        print(n)
        print_num(n-1)

n = int(input("Enter a number: "))
print_num(n)

'''
Sir's function 

def print_num(n):
    if n == 0:
        return
    print(n)
    print_num(n-1)
'''