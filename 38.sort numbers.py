# Assigment  รับเเละเรียงลำดับตัวเล

number = []
 
while True:
    x = int(input("ป้อนตัวเลข : "))
    if x <= 0:
        break
    number.append(x)

number.sort()     # => .sort() = เรียตัวเลขจากน้อยไปมาก
print(number)

number.reverse()  # => .reverse = เรียตัวเลขจากมากไปน้อย
print(number)