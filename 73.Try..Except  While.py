
while True:
    try:
        number1 = int(input("ป้อนตัวเลข "))
        number2 = int(input("ป้อนตัวเลข "))
        if number1 == 0 and number2 == 0:
            break
        result = number1 / number2
        print(result)
    except  ValueError:
        print("ต้องป้อนตัวเลขเท่านั่น")
    except ZeroDivisionError:
        print("ห้ามใส่เลขศูนย์")
    finally:
        print("โปรแกรมทำงานสำเร็จ")