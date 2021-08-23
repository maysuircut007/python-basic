data = {"191":"แจ้งเหตุด่วน", "1668":"รถพยาบาล", "1447":"ดับเพลิง"}

def serchNumber(massage):
    for key, value in data.items():
        if value == massage:
            print("เบอติดต่อ", key)
        else:
            pass
massage = input("ป้อนข้อมูลที่ต้องการ : ")        
serchNumber(massage)

