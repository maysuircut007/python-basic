import random


atm_password = "54"
result = "" # เก็บค่า

while result != atm_password:
    result = ""  # เก็บค่าใน loop
    for letter in range(len(atm_password)):
        list_number = random.choice("0123456789abcdefghijklmnopqrstuvwxyz")
        result = "".join(list_number) + str(result) # หรือ result.join(list_number) + str(result)
        print("Searh ",result)

print("crack password is ",result )