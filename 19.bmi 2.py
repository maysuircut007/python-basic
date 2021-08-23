

#input
weight = int(input("ป้อนน้ำหนักของคุณ : "))
high = int(input("ป้อนส่วนสูงของคุณ : ")) / 100 #เเปลงเป็นเมตร


#process
bmi = weight / high**2


'''
18 = ต่ำกวา่เกณฑ์
18.5 - 22.9 = สมส่วน
23.0 - 24.9 = น้ำหนักเกิน
25.0 - 34.9 = โรคอ้วนระดับ 1
> 30 = โรคอ้วนระดับอันตราย
'''

if bmi > 0 and bmi <= 18:
    resule = "ต่ำกวา่เกณฑ์"
elif bmi >= 18.5 and bmi <= 22.5:
    resule = "สมส่วน"
elif bmi >= 23.0 and bmi <= 39.9:
    resule = "น้ำหนักเกิน"
elif bmi > 30:
    resule = "โรคอ้วนระดับอันตราย"
else:
    resule = "ไม่ทราบค่าที่ชัดเจน"

print("ค่า bmi =", bmi, "ผลคือ", resule)