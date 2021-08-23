 # Recursive Function

# เรียกซ้ำ Function

'''
หาจุกทำซ้ำ
หาจุดออกจาก function
ต้องมี parameter
'''


def addNumber(number):  # => parameter
    if number == 5:     # =>  จุดออกจาก function
        return
    print(number )
    number += 1
    addNumber(number)    # => หาจุกทำซ้ำ
 
addNumber(0)

def summation(number): # => parameter
    if number == 1:     
        return number    # =>  จุดออกจาก function
    else:
        return number + summation(number - 1) # => หาจุกทำซ้ำ
    
x = summation(5)
print(x)