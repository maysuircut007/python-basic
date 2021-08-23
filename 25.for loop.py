

# โครงสร้างควบคุมเเบบทำซ้ำ
                   #range(start, stop, step)
for i in range(5): # => index 0 1 2 3 4  
    print("รอบที่", i, "Hello world")

sumation1 = 0
for j in range(1, 6): # => index 0 1 2 3 4 5 
    sumation1 += j
    print("รอบที่", j, "sum", sumation1)

sumation2 = 0
for k in range(1, 6, 2): # => index 0 1 2 3 4 5 
    sumation2 += k
    print("รอบที่", k, "sum", sumation2)


sumation3 = 0
for l in range(10, 0, -1): # => index 0 1 2 3 4 5 
    sumation3 += l
    print("รอบที่", l, "sum", sumation3)