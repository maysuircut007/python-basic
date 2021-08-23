

i = 1
sumation = 0
count = int(input("ระบุจำนวนรอบ : "))
while i <= count:
    sumation += i 
    print("รอบที่", i, "ค่า sum = ", sumation)
    i += 1

average = sumation / count
print("ผลรวมการบวก = ", sumation)
print("ค่าเแลีย", average)

     