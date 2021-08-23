#  Exception

'''
try:
    คำสั่งรันโปรเเกรม
except:
    คำสั่งตอนที่โปรแกรมมีข้อผิดพลาด
'''

try:
    number1 = int(input("ป้อนตัวเลข "))
    number2 = int(input("ป้อนตัวเลข "))
    result = number1 / number2
    print(result)
except Exception as e: 
    print(e)
#else:
    #print("โปรแกรมทำงานสำเร็จ")
finally:
    print("โปรแกรมทำงานสำเร็จ")


#except:
    '''
    print("โปรแกรมมีข้อผิดพลาด")
    '''
#  จัดการ Exception หลายเหตุการณ์
'''
except ValueError:
    print("ต้องป้อนตัวเลขเท่านั่น")
except TypeError:
    print("ข้อมูลไม่ถูกต้อง")
except ZeroDivisionError:
    print("ห้ามใส่เลขศูนย์")
'''
#การเขียนลดรูป Exception

