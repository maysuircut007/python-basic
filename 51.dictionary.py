
# dictionary => key(การเข้าถึงข้อมูล),  value(ค่าของข้อมูล)
# การสร้าง dictionary
# ชื่อตัวเเปร = {key:value, key:value, key:value}

colors = {"red":"สีเเดง", "yellow":"สีเหลือง", "green":"สีเขียว", 98:"บ้านเเสนสุข", 100:"บ้านป่า"}
'''
print(colors["yellow"])
print(colors[98])
'''
animal = {"ไก่":"chicken", "แมว":"cat", "dog":"หมา"}
'''
print(animal["แมว"])
'''
# constructor
pets = dict(cat="แมว", dog="หมา", chicken="ไก่") # => dict(ตัวเเปร = value)
pets1 = dict({"dog":"น้องหมา","cat":"น้องแมว", "chicken":"น้องไก่"}) # => dict(key:value)
statat = dict({True:"โสด", False:"สมรส"})
'''
print(pets["cat"])
print(True)
'''
# การแก้ไขข้อมูล
'''
colors[98] = "บ้านเเสนสบาย"
print(colors)
'''

# การเพิ่มข้อมูล
'''
colors.update({"blue":"สีน้ำเงิน", "red":"สีชมพู"})
print(colors)
'''

                  # การลบข้อมูล
# .pop()
'''
colors.pop("red")
print(colors)
'''
# .popitem()
'''
colors.popitem() # ลบข้อมูลที่เพิ่มล่าสุด หรือตัวหลังสุด
print(colors)
'''
# .clear การลบสมาชิก
''' 
colors.clear() # => การลบสมาชิก
print(colors)
'''
# del
'''
del colors
print(colors)
'''

# การคัดลอก
# .copy
'''
x = colors.copy()
print(x)
'''

# loop
'''
for item in colors:
    print(item)  # => จะเเสดงเฉพาะ key
'''
'''
for item in colors.keys():
    print(item)  # => จะเเสดงเฉพาะ key
'''
'''
for item in colors.values():
    print(item)  # => จะเเสดงเฉพาะ value
'''

for x, y in colors.items():
    print(x, y)  # => จะเเสดง 

# nested dictionaty
market = {
    "ร้านป้าพร":{
        "name":"ป้าพร",
        "menu":["กะเพราไก่", "ก๋วยเตี๋ยว"],  # => list
        "zone":"ตะวันออก"
    },
    "ร้านลุงป้อม":{
        "name":"น้าจ๊อบ",
        "menu":["มะม่วง", "ทุเรียน"],  # => list
        "zone":"ทางเข้าตลาด"
    },
    "ร้านน้าใจ":{
        "name":"น้าใจ",
        "menu":["นมปั่น", "ชาเย็น"], # => list
        "zone":"ข้าง 7 - 11"
    }
}
'''
print( "ก๋วยเตี๋ยว" in market["ร้านป้าพร"]["menu"])

if "ก๋วยเตี๋ยว" in market["ร้านป้าพร"]["menu"]:
    print("เป็น")
else:
    print("ไม่เป็น")
'''

