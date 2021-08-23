# เเปลงอุณหภูมิ
# c =  (f - 32) * 5 / 9
# f = (c * 9 / 5) + 32 

data = input("ป้อนองศา : ") 
temp = int(data[:-1])
symbal = data[-1].upper()

if symbal == "C":
    t = (temp * 9   / 5) + 32 
    text = "องศาฟาเรนไฮ"
    text2= "องศาฟาเซลเซียส"
elif symbal == "F":
    t =   (temp - 32) * 5 / 9
    text = "องศาฟาเซลเซียส"
    text2 = "องศาฟาเซลเซียส"
else:
    print("ไม่ทราบข้อมูล")

print(temp, text2 + "ของคุณ = ", t, text)