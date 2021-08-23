# การใช้ Set
fruit = {"มะม่วง","มะม่วง", "มะขาม", "มะยม", 50, True}

'''
print(fruit)
print(type(fruit))
'''
# constructor
fish = set(["ปลาดุก", "ปลาหมอ"])
'''
print(fish)
'''
# แปลงข้อมูล
lis = [12, 34, 54, 54, 54, 65, 12, 65, 34]
'''
print("lis = ", lis)
lis = set(lis)
print("set = ", lis)
'''
# เพิ่มข้อมูลสมาชิก .add()
'''
fruit.add("ทุเรียน")
fruit.add("สัปปะรด")
fruit.add(999)
print(fruit)
'''

# เพิ่มข้อมูลสมาชิกหลายตัว  .update()
'''
fruit.update(lis) # => หรือกรณีไม่มีตัวแปล fruit.update([12, 34, 54, 54, 54, 65, 12, 65, 34]) 
print(fruit)
'''

# loop
'''
for item in fruit:
    print("ข้อมูล ", item)
'''

# เเสดงจำนวนสมาชิก len()
'''
print(len(fruit))
'''
# การค้นหาข้อมูล
'''
if "มะเฟือง" in fruit:
    print("มี")
else:
     print("ไม่มี")

print("มะเฟือง" in fruit)
print("มะเฟือง" not in fruit)
'''

                    # การลบ set
# .remove()
'''
fruit.remove("มะม่วง")
print(fruit)
'''
# .discard()
'''
fruit.discard(fruit)  # => แม้ไม่มีข้อมูลก็ไม่ error
print(fruit)
'''
# .clear()
'''
fruit.clear() # => ลบข้อมูลภายใน
print(fruit)
'''
# del
'''
del fruit  # => ลบตัวเเปล 
print(fruit)
'''


