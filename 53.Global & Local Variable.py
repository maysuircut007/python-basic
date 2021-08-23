# Global & Local Variable

def displayNumber():
    x = 10   # =>  Local Variable
    print("Hello", x)


x = 20 # =>  Global Variable
displayNumber()  
print("Hello", x)