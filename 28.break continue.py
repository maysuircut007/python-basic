


i = 1
while i <= 10:
    print("รอบที่ : ", i)
    if i == 5:
        break   # i = 5 => กระโดดออกจากลูป
    i += 1
print("จบโปรเเกรม")


i = 1
while i <= 10:
    i += 1
    if i == 5:
        continue   # เมื่อ i = 5 => กระโดดข้าม
    print("รอบที่ : ", i)
print("จบโปรเเกรม")


i = 1
while i <= 10:
    print("รอบที่ : ", i)
    i += 1
    if i % 2 != 0:
        continue   # เมื่อ i = 5 => กระโดดข้าม
print("จบโปรเเกรม")