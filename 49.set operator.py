

fruitA = {"กล้วย", "มะยม", "มะนาว", "กีวี่", "บลูเบอรี่"}
fruitB = {"สตอเบอรี่", "กีวี่", "บลูเบอรี่", "กล้วย"}

# .union()
'''
Allfruit = fruitA.union(fruitB)
print(Allfruit)
'''
# .update()
'''
fruitA.update(fruitB)
print(fruitA)
'''

# .copy()
'''
fruitC = fruitB.copy()
print(fruitC)
'''

# .difference()
'''
fruitC = fruitA.difference(fruitB) # เเสดงสมาชิก fruitA ที่ไม่มีใน fruitB
print(fruitC)
'''

# .intersection()
'''
fruitC = fruitA.intersection(fruitB) # เเสดงสมาชิก fruitA ที่มีใน fruitB
print(fruitC)
'''
# .difference_update
'''
fruitA.difference_update(fruitB) # เก็บข้อมูลที่ fruitA ไม่มีใน fruitB 
print(fruitA)
'''

# .intersection_update()
'''
fruitA.intersection_update(fruitB) # เก็บข้อมูลที่ fruitA มีใน fruitB fruitA  
print(fruitA)
'''

# superset
fish = {"ปลาหมอ", "ปลาดุก", "ปลาวาฬ", "ปลาโมา", "ปลาแลาม", "ปลาตะเพียน"}
#subset
x = {"ปลาหมอ", "ปลาซิว"}
y = {"ปลาหมอ", "ปลาดุก"}
'''
print(x.issubset(fish)) # => Fales
print(y.issubset(fish)) # => True
print(fish.issuperset(x)) # => Fales
print(fish.issuperset(y)) # => True
'''

# min max
number = {2,12,51,25,521,487,85,5,5,58,57,47,57,47,485,87,78,92,2,}
'''
print(min(number))
print(max(number))
'''