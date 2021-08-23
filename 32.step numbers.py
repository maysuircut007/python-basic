

number = int(input("ป้อนตัวเลข = "))

for row in range(1, number + 1):
    for colum in range(1, row + 1):
        print(colum, end = " ") # => end "จบค้วยช่องว่างขึ้นบรรทัดใหม่" 
    print(" ")