import os

try:
    if os.path.exists("78.score.txt"):
        os.remove("78.score.txt")
        print("ลบเรียบร้อย")
    else:
        print("ไม่พบไฟล์")
except Exception as e:
    print(e)
