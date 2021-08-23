# ฟังก์ชั่นเช็คจำนวนตัวอักษร
 
from abc import abstractmethod


def checkstring(massage):
    result = {"UPPER":0, "LOWER":0}
    for i in massage:
        if i.isupper():  
            result["UPPER"] += 1
        elif i.islower():
            result["LOWER"] += 1
        else:
            pass
    return result


massage = input("input you massage : ")
x = checkstring(massage)
print(x)