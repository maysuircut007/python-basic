
#data type and variable
                                                   
                                    #primitive data type#
s = "ผลลัพธ์ ="                   # => string
x = 20                           # => integer             
y = 3.9                          # => floating poin              
z = True                         # => boolean

'''  
         #type conversion                    #กฎการตั้งชื่อ
    เเปลงเป็น string  =>  str()            1.ใส่ ตัวเลข ตัวอักษร เครื่องหมาย
    เเปลงเป็น integer =>  int()            2.ห้ามขื้นต้นด้วย ตัวเลข เครื่องหมาย สัญลักษณ์ ยกเวัน _
    เเปลงเป็น floating poin =>  float()    3.ห้ามซ้ำกับ keyword
                                         4.case sensitive
'''

print(x)
print("ตอบ", s, x)
print("ตอบ", s, str(x))       # =>  เเปลง x เป็น string
print("ตอบ", s, float(x))     # =>  เเปลง x เป็น floating poin

print(y)                      
print("ตอบ", s, y)
print("ตอบ", s, int(y))       # =>  เเปลง y เป็น integer


#แสดงชนิดข้อมูล
print(type("Maysa kumnerddee"))
print(type(s))
print(type(x))
print(type(y))
print(type(z))