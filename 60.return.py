
# return


def randonNumber(x):
    if len(x) < 3:
        return
    if x == 100:
        print("ถูกหวย")
        return 1000  # => ส่งค่าออกไป 1000
    else:
        print("ไม่ถูกหวย")
        return 0     # => ส่งค่าออกไป 0

money = randonNumber("10")
print("เงินรางวัล", money)