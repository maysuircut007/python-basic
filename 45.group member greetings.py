#  กลุ่มสมาชิกคำทักทาย

greeting = ["สวัวดี", "hi", "hello", "goodby"] 
peple = ["ก้อง", "แก้ม", "โจ้"]
resual = []
for x in greeting:
    for y in peple:
        resual.append(x + y)

print(resual)