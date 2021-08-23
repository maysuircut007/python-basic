# frozen set เปลียนเเปลงข้อมูลไม่ได้

fruit = frozenset(["มะม่วง", "มะนาว", "มะยม"])
print(fruit)
fruit = list(fruit)
print(type(fruit))
fruit = frozenset(fruit)
print(type(fruit))

for item in fruit:
    print("ข้อมูล",item)
    