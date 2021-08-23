#โปรเเกรมคำนวน bmi (ดัชนีมวลกาย)
#สูตร น้ำหนัก / ส่วนสูง * ส่วนสูง (m)


#input
weight = int(input("ป้อนน้ำหนักของคุณ : "))
high = int(input("ป้อนส่วนสูงของคุณ : "))
high /= 100 #เเปลงเป็นเมตร


#process
bmi = weight / high**2
print(bmi)

