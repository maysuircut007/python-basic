fname = "maysa"
lname = "kemnerddee"
age = "29"
saraly = 1000.213546879

# การต่อ string   concatinate (+)
print("ชื่อ : " + fname + "\tนามสกุล : " + lname + "\tอายุ : " + age)


# การจัดรูปแบบการเเสดงผล {}
# function format
text = "ชื่อ : {} \tนามสกุล : {} \tอายุ : {} "
print(text.format(fname, lname, age))

text_2 = "ชื่อ : {1} \tนามสกุล : {0} \tอายุ : {2} \tอาชีพ : {3} \tเงินเดือน : {4:.2f}"
print(text_2.format(fname, lname, age, "วิ่งว่าว", saraly)) # => index = 0 1 2 3


# นับจำนวนคำในประโยค
# function  count
fruit = "ไปซื้อผลไม้ มีทุเรียน มังคุด ข้าวเหนียวทุเรียน ที่ตลาด จะแวะไปสวนทุเรียน "
print(fruit.count("ทุเรียน"))


# เช็คคำชึ้นต้น / ลงท้าย
# function startswith => เช็คคำชึ้นต้น
# function endswith =>  เช็คคำลงท้าย
name = "นาย เมษา กำเหนิดดี"
x = name.startswith("นาย")

if x:
    print("คุณเป็นผู้ชาย")

if name.endswith("ดี"):
    print("ก็ดีนะ", 9/4)
