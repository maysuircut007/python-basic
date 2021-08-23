
# การส่งค่าเข้ามาในฟังก์ชั่น

def myData(name, lname, old):
    print("ชื่อ : ", name, "นามสกุล", lname, "อายุ", old)


fname = "maysa"
lname = "kumnerddee"
age = 29
myData(fname, lname, age)

def addition(x, y):
    print("ผลรวม",x + y)

x = 5
y = 9

addition(x, y)


# Arguments => ค่าที่ส่งเข้าไปใน fucntion => fname, lname, age (ตอนที่เรียกฟังชั่น)
# Parameter => ค่าตัวเเปลที่รับข้อมูลส่งมาทำงาน (Arguments) => fname, lname, age
# อาส่ง - พารับ