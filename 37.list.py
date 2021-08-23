
# non primitive data type : list

# index          =>   |0 |1 |2 |3 | 4 |      length = 5 
# negative index =>   |-5|-4|-3|-2|-1 |

number = [] #list ว่าง
number = [1, 2, 3, 4, 5, 6, 6] # list มีสมาชิก integer 1 2 3 4 5 6
name = ["นาย A", "นาย B", "นาย C"] # list มีสมาชิก string 
All = [10, "นายไข่", True, 3.14, -10] # list มีสมาชิก string, integer, floating poin, 


# แสดงผล
'''
print(name)
print(number)
print(All)
print(type(name))
'''
# ประกาศข้อมูลเเบบ constructor
'''
name = list(["นาย A", "นาย B", "นาย C"]) # name = list([])
'''
# การเข้าถึงข้อมูล  list
'''
print(All[0])  # print(number[-6])
print(All[0] + number[1])
print(All[1:4])
print(All[-4:-1])
print(All[-4:])  # จนถึตัวสุดท้าย
print(All[:5])
'''
# การเเก้ไขข้อมูล
# ชื่่อตัวเเปล[] = ข้อมูลใหม่
'''
number[1] = 9
number[-1] = "นายกล้วย"
print(number)
'''
# การใช้ loop

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''
sum = 0
for x in num:
    sum += x
    print(x)
print(sum)
'''

# การตรวจสอบช้อมูล
fruit = ["มะยม","มะนาว","มะพร้าว"]
'''
if "มะนาว" in  fruit:
    print("ใช้")
else:
    print("ไม่ใช้")
'''
# นับจำนวนสมาชิก len()
'''
print(len(fruit))
'''
# len() ร่วมกับ for loop
'''
for i in range(len(fruit)):
    print(i)
    print(fruit[i])
'''
           # การเพิ่มขัอมูล
# การเพิ่มขัอมูล .append()
'''
fruit.append("มะละกอ")
print(fruit)
'''
# การเพิ่มขัอมูล .insert()
# ตัวเเปล.insert(index, สมาชิกใหม่)
'''
fruit.insert(1, "มะปราง")
print(fruit)
'''
           # การลบข้อมูล

#  การลบข้อมูล .remove()
'''
fruit.remove("มะนาว")
print(fruit)
'''
# การลบข้อมูล .pop() => ลบข้อมูลตัวสุดท้าย
'''
fruit.pop()
print(fruit)
'''
# การลบข้อมูล del 
#  del ตัวเเปล[index]
'''
del fruit[2]
print(fruit)
'''
#  del ตัวเเปล  => ลบตัวเเปล
'''
del fruit
print(fruit)
'''
# การลบข้อมูล clear => ลบข้อมูลภายใน list ทั่งหมด
'''
fruit.clear()
print(fruit)
'''
# การคัดลอก .copy
'''
x = fruit.copy()
print(x)
'''
# การรวมข้อมูล
'''
Allgroup = number + fruit
print(Allgroup)
'''
# การรวมข้อมูล extend
'''
number.extend(fruit)
print(number)
'''
# แสดงจำนวนสมาชิก
'''
x = number.count(6)
print(x)
'''