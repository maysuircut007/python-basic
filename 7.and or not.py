# logical ตัวดำเนินการทางตรรกศาสตร์
# and, or, not
# คำตอบที่ได้ => true, false

x = 5 > 10  # => ค่าเป็น bool => false
y = 5 >= 2  # => ค่าเป็น bool => true
print(x, y)
 
z = x == y  # => ค่าเป็น bool => false
n = x != y  # => ค่าเป็น bool => true
print(z)
print(n)


#and
a = x and y  # => ค่าเป็น bool => false
print(a)


#or 
b = x or y  # => ค่าเป็น bool => false
print(b)

#not  กลับค่า
b = not b
print(b)

c = not x, not y
print(c)

print(not n)