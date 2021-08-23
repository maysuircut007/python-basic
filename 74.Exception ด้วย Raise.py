while True:
    try:
        name = input("ใส่ชื่อของคูณ")
        if name == "maysa":
            raise Exception("ชื่่อขงคุณถูกเเบน")
            break
        number1 = int(input("ป้อนตัวเลข "))
        number2 = int(input("ป้อนตัวเลข "))
        if number1 == 0 and number2 == 0:
            break
        if number1 < 0 or number2 < 0:
            print("ไม่สามารถป้อนค่าติดลบได้")
            break
        result = number1 / number2
        print(result)
    except  Exception as c:
        print(c)
         