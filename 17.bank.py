
# แลกเงินและหาจำนวนแบงค์

bank = int(input("ป้อนจำนวนเงิน : "))

if bank >= 1000:
    bank  // 1000
    print("ใบพันจำนวน", bank  // 1000, "ใบ")
    bank %= 1000 # ส่งค่าตัวเเปรออกจาก if เอาเศษไปใช้ใน if ถัดไป

if bank >= 500:
    print("ใบห้าร้อยจำนวน", bank // 500, "ใบ")
    bank %= 500 # ส่งค่าตัวเเปรออกจาก if เอาเศษไปใช้ใน if ถัดไป

if bank >= 100:
    print("ใบร้อยจำนวน", bank // 100, "ใบ")
    bank %= 100 # ส่งค่าตัวเเปรออกจาก if เอาเศษไปใช้ใน if ถัดไป

if bank >= 50:
    print("ใบห้าสิบจำนวน", bank // 50, "ใบ")
    bank %= 50 # ส่งค่าตัวเเปรออกจาก if เอาเศษไปใช้ใน if ถัดไป

if bank >= 20:
    print("ใบยี่สิบจำนวน", bank // 20, "ใบ")
    bank %= 20 # ส่งค่าตัวเเปรออกจาก if เอาเศษไปใช้ใน if ถัดไป
