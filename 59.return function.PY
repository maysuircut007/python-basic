 #function return ค่า

'''
1.ไม่มีการรับส่งค่า
def name():

2.มีการรับค่าเข้าไปทำงาน
def name(a, b)

3.มีการรับค่าเข้าไปทำงาน และส่งค่าออกมา
def name(a, b):
    return a + b

4. ไม่มีการรับส่งค่าเข้ามา เเต่ส่งค่าออกไป
'''

def add(a, b):
    return a + b 

def showNumber():
    return 500

x = showNumber() 
print("ตัวเลข = ", x)
print(showNumber())

def randonNumber(x):
    if x == 100:
        print("ถูกหวย")
        return 1000  # => ส่งค่าออกไป 1000
    else:
        print("ไม่ถูกหวย")
        return 0     # => ส่งค่าออกไป 0

money = randonNumber(100)
x = 300
result = money - x
print("เงินรางวัล", money)
print("เงินคงเหลือ",result)