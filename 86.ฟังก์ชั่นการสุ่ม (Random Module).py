import random
'''
x = random.random()
for i in range(15):
    print(x)
'''
'''
for i in range(15):
    x = random.uniform(-10, 5)
    print(x)
'''
'''
for i in range(15):
    x = random.randrange(-5, 10, 2) # start, stop, stap
    print(x)
'''
'''
for i in range(15):
    x = random.randrange(-5, 10, 2) # start, stop, stap
    print(x)
'''
'''
for i in range(15):
    x = random.randint(-5, 10, ) # start, stop จำนวนเต็ม
    print(x)
'''
'''
items = [1, 2, 3, 4, 5, "A", "B", "c",]
for i in range(15):
    x = random.choice(items) # สุ่มในลิส items
    print(x)
'''
'''
random.shuffle(items) # สุ่มสลับค่า
print(items)
'''
'''
for i in range(15):
    x = random.choice("0123456789") 
    print(x)
'''