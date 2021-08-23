# List Parameter

def displayfruit(item):
    for i in range(len(item)):
        print("ผลไม้ชิ้นที่ ", i + 1, "=", item[i])

def displayvet(item):
    for i in range(len(item)):
        print("ผลไม้ชิ้นที่ ", i + 1, "=", item[i])
        
fruit = ["มะม่วง", "มะละกอ", "ฝรัง", "มะนาว"]
vet = ("ชะอม", "ผักกาด", "คะน้า")

displayfruit(fruit)
displayvet(vet)