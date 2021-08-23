 # ฟีโบนัชชี (Fibonacci)


def fibonacci(number):
    if number <= 1:
        return number
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)

for i in range(1):
    print(fibonacci(i))
