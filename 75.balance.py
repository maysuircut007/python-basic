
account = {"นายA":5000, "นายB":0}

def getBalance():
    print("ยอดเงินคงเหลือในบัญชี ", account)

def deposit(money):
    if type(money) is not int and type(money) is not float:  # not type(money) is int
        raise Exception("ป้อนตัวเลขเท่านั้น")
    if money <= 0:
        raise Exception("ค่าตัวเลขเป็นบวกเท่านั่น")
    print("ฝากเงินเข้าบัญชี A ", money)
    account["นายA"] += money

def withdraw(money):
    if type(money) is not int and type(money) is not float:  # not type(money) is int
        raise Exception("ป้อนตัวเลขเท่านั้น")
    if money <= 0:
        raise Exception("ค่าตัวเลขเป็นบวกเท่านั่น")
    if money > account["นายA"]:
        raise Exception("ยอดเงินไม่พอ")
    print("ถอนเงินออกจากบัญชี A", money)
    account["นายA"] -= money

def transfer(money):
    if type(money) is not int and type(money) is not float:  # not type(money) is int
        raise Exception("ป้อนตัวเลขเท่านั้น")
    if money <= 0:
        raise Exception("ค่าตัวเลขเป็นบวกเท่านั่น")
    if money > account["นายA"]:
        raise Exception("ยอดเงินไม่พอ")
    print("ทำการโอนเงินไปที่บัญชี B", money)
    account["นายB"] += money
    account["นายA"] -= money


try:
    getBalance()
    #deposit(500)
    #withdraw(10000)
    transfer(7.2)
    print(account)
except Exception as e:
    print(e)
