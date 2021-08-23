#  Anonymous function or lambda function

def myPower(x):
    return lambda a: x**a

y = myPower(5)
result = y(2)
print(result)


