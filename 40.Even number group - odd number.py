
# Assigment  กลุ่มเลขคู่ - เลขคี่

number = []
odd = []
even = []

while True:
    x = int(input("ป้อนตัวเลข"))
    if x < 0:
        break
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)
    number.append(x)

print("ค่าทั้งหมด : ", number)
print("เลขคี่ : ", odd)
print("เลขคู่ : ", even)