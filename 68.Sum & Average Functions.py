# ฟังก์ชั่นหาผลรวม & ค่าเฉลี่ยตัวเลข

def sumMation(number):
    total, avr = 0, 0
    for i in number:
        total += i
    avr = total / len(number)
    return total, avr

x = [1, 2, 3, 4, 5, 6]
y, z = sumMation(x)

print(y)
print(z)