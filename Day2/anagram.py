s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")

def anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    s1 = sorted(s1)
    s2 = sorted(s2)

    return s1 == s2 
print(anagram(s1, s2))