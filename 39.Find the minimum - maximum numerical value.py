
# Assigment หาค่าตัวเลขต่ำสุด - สูงสุด - ผลรวม
number = []
while True:
    x = int(input("ป้อนตัวเลข : "))
    number.append(x)
    if x <0:
        break
print("ค่ามากสุด : ", max(number))
print("ค่าน้อยสุด : ", min(number))