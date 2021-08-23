import datetime

time = datetime.datetime.now()
#print(time)

newtime = datetime.datetime(2021, 7, 28, 15) # => yyyy,m,d,time
#print(newtime)

# รูปเเบบกเรเเสดงผล
'''
print("เริ่มต้น", time)
print(time.strftime("%x"))  # m/d/y  เเบบสั้น
print(time.strftime("%X"))  # เวลา  เเบบสั้น
print(time.strftime("%c"))  # ชื่อวัน ชื่เดือน เวลา
'''

# เวลา
#print(time.strftime("%H:%M:%S:%p"))

# 1- 366
#print(time.strftime("%j")) 

# date
'''
print(time.strftime("%a")) # วันเเบบสั้น
print(time.strftime("%A")) # วันเเบบเต็ม
print(time.strftime("%w")) # 0 = sunday 
print(time.strftime("%d")) # วันที่
print(time.strftime("%b")) # เดือนเเบบสั่น
print(time.strftime("%B")) # เดือนเเบบเต็ม
'''
#print(time.strftime("วัน %A ประจำวันที่ %d เดือน %B ปี %Y"))


# ว/ด/ป
#print(time.strftime("%d / %m / %Y"))