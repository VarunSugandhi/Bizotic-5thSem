"""
Dictionary will be given and we have to find the avg marks for each student and print it along with the name of topper and his marks 
"""

dict = { "Alice" : [80,70,90,85,75] , "Bob" : [60,55,45,70,65], "Charlie" : [90,95,88,92,85] }

for k , v in dict.items() :
    print(f"The avg scores for {k} is: {sum(v)/len(v)}")

highest_marks = -1
name = ""

for k , v in dict.items():
    maximum_scr = max(v)
    if maximum_scr > highest_marks :
        highest_marks = maximum_scr
        name = k

print(f"\nTopper is {name} with {highest_marks} marks")