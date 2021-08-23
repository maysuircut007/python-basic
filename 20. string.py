
#  loger |0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|

# การเข้าถึงอักษรใน string
name = "Maysa kumnerddee" #index คือตำเเหน่ง string เริ่ม 0 , 15 หรือ  -16 , -1
'''
print(name[0])
print(name[:3]) # หรือ (name[0:3]) = May
print(name[6:])  #  หรือ(name[6:15]) = kumnerddee
print(name[5:6]) # ช่องว่าง => 5 เท่ากับช่องว่าง
print(name[:-1]) # หรือ (name[-16:-1]) = Maysa kumnerddee
print(name[-16:]) # หรือ (name[-16:-1]) = Maysa kumnerddee
print(name[-10:-4])  #  = kumnerd
'''

# len function => หาความยาว string

'''
print(len(name))
'''

# strip function => ลบช่องว่างซ้ายขวา
nickname = "  may  "
#print(len(nickname))
#nickname = nickname.strip()
#nickname = nickname.lstrip() # lstrip function => ลบช่องว่างซ้าย
#nickname = nickname.rstrip() # rstrip function => ลบช่องว่างซ้าย
print(nickname)


# แปลงเคสของ string
# lower function   =>  แปลง string เป็นตัวใหญ่
# upper function   =>  แปลง string เป็นตัวเล็ก
# capitalize function   => แปลง string ตัวเเรกเป็นตัวใหญ่
lname = "kumnerddee"

print(lname.lower())
print(lname.upper())
print(lname.capitalize())



# replace function  การแทนที่ 
grade = "maysa kumnerddee เกรด 4 อยู่ชั้นปี 4 อยู่ซอย 4"
'''
print(grade.replace('4', '3.5'))
print(grade.replace('4', '3', 2))
'''
# การเช็คข้อความ
'''
x = "เกรด" in grade # => boolean
print(x)

if x:
    grade = grade.replace("เกรด", "ควย")

print(grade)
'''