# tuple = ()
tup = (1, 2, 3, 4)
tup1 = ("maysa kumnerddee", "may", 10, 2535, 19098, True, False)

# constructor
tup2 = tuple((1, 2, 3, 4))

# การดูคลาสของ tuple
print(type(tup))

# การเข้าถึงข้อมูล
'''
print(tup[0:4])
print(tup[2])
print(tup[-3])
print(tup[:-1])
print(tup[1:])
'''

# การเเก้ไขข้อมูล
'''
lis = [1, 1, 2, 2, 23, 5, 8, 8] # => list
print(type(lis)) 

lis = tuple(lis) # แปลง List เป็น tuple   
print(type(lis))

lis = list(lis)
print(type(lis)) #  แปลง tuple เป็น List
'''

# การแสดงผลด้วย loop
'''
for item in tup1:
    print(item)

# การตรวจสอบข้อมูล
if "may" in tup1:
    print("เป็นสมาชิก")
else:
    print("ไม่เป็นสมาชิก")
'''
# การนับจำนวนสมาชิก
'''
print(len(tup1))
'''
# len() ทำงานรวมกับ loop for
'''
for i in range(len(tup1)):
    print(tup1[i])
'''
                #  การสร้างและเพิ่มข้อมูล (join)
'''
x = () # => การสร้าง tuple ว่าง
print(type(x))
x = ("maysa") # => เป็น string เพราะ ไม่มี (,)
print(type(x))
x = ("maysa",) # => เป็น tuple เพราะ มี (,)
print(type(x))
'''
# การบวก tuple
'''
name = ("maysa kumnerddee", "may") # => tuple
new = "mayse" #  => string

name = name + (new,) # => (new,) = tuple(new) = การแปลง string เป็น tuple
print(name)   
''' 
#  การทำงานร่วมกับ list
'''
tup3= ("maysa kumnerddee", "may", 10)                  
city = ["กรุงเทพ", "ชลบุรี", "อุบล"]

All = tup3 + tuple(city)
print(All)
'''
                    # การลบ tuple
tup = (1, 2, 3, 4)
# การใช้ del
'''
del tup # => ลบตัวเเปลอ tuple
print(tup)
'''
# การใช้ .pop()

'''
tup= list(tup) # แปลงให้เป็น list ก่อน
tup.pop() 
print(tup)
tup= tuple(tup) # แปลงกลับให้เป็น tuple
'''
# การใช้ .remove()
'''
tup= list(tup) # แปลงให้เป็น list ก่อน
tup.remove(2) 
print(tup)
tup= tuple(tup) # แปลงกลับให้เป็น tuple
print(type(tup)
'''
# การค้นหาเเละนับจำนวนสมาชิก
'''
x = tup.count(4) # => เลข 4 มีกี่ตัว
print(x)
x = tup.index(4) # => หาตำเเหน่ง index ของ 4
print(x)
'''
             # การเรียงลำดับข้อมูล
# การใช้ .sort()
#tup = (100, 105, 12, 1, 2, 3, 4, 4, 3, 2, 1, 5, 4, 545, 545, 43)
'''
tup= list(tup) # แปลงให้เป็น list ก่อน
tup.sort() # เรียงจากน้อยไปมาก
tup = list(tup) # แปลงกลับให้เป็น tuple
print(tup)
'''
# การใช้ .reverse()
'''
tup= list(tup) # แปลงให้เป็น list ก่อน
tup.reverse()  # เรียงกลับ
tup = list(tup) # แปลงกลับให้เป็น tuple
print(tup)
'''
# การใช้ reversed() => string to tuple
'''
x = "maysa kumnerddee"
y = tuple(reversed(x))
print(y)
'''

# การนำ tuple ใส่ในตัวเเปล
'''
a, b, c, d = tup
print(a)
print(b)
print(c)
print(d)
print(a + b)
'''
# การสลับ tuple
'''
x = 50, 60
y = 70, 80
print(x, y)
x,y = y,x
print(x, y)
'''
# การรวม string โดยใช้ .join()

charactor = ("m", "a", "y")
print(charactor)
may = "".join(charactor)
print(may)


