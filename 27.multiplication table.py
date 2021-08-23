# แม่สูตรคูณ


start = int(input("เเม่เเรก : "))
stop = int(input("แม่สุดท้าย : "))

for x in range(start, stop):
    print("แม่", x, "ได้แก่")
    for y in range(1, 13):
        print("แม่", x, "x", y, "เท่ากับ", x * y)

