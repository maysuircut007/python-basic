

import random

myrandom = random.randrange(1, 7)
k = 1
correct = False
while True:
    number = int(input("ป้อนตัวเลข : "))
    correct = myrandom == number
    if not correct:
        if number < myrandom:
            print("มากกว่า")
        else:
            print("น้อยกว่า")
    
    if correct:
        print("คุณรับไปเลย 1 ล้านบาท")
        break
    if number < 0 or k == 3:
        break
    k += 1


if not correct:
    print("เสียใจด้วยนะ")
    print("เฉลย", myrandom)