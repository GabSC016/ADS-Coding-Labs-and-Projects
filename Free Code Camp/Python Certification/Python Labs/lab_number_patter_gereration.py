# Lab: Build a Number Pattern Generator
# In this lab you will practice the basics of Python by building a small app that creates a number pattern.

def number_pattern(n):
    if not isinstance(n,int):
        return "Argument must be an integer value."
    elif n < 1:
        return "Argument must be an integer greater than 0."
    else:
        ints_list=[]
        for num in range(1,n+1):
            ints_list.append(str(num))
    return " ".join(ints_list)

print(number_pattern(4))