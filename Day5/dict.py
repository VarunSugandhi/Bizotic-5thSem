# Dictionary in Python
#Printing the frequency of each word in the string

s = "the cat sat on the mat the cat"
dict = {}

for word in s.split() :
    if word not in dict:
        dict.setdefault(word, 1)
    else :
        dict[word] += 1

print("The String is: ",s)
print("The frequency of each word in string is: ")
for k,v in dict.items():
    print(k, " " , v)