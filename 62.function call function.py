# ฟังก์ชั่นเรียกฟังก์ชั่น

def compareMax(x, y):
    if x > y:
        return x
    else:
        return y

def equal(x, y, z):
    a = compareMax(x, y)   # return compareMax(compareMax(x, y) z)
    m = compareMax(a, z)
    return m

max = equal(10, 20, 30)
print(max)


def displayFood():
    print("หูฉลาม")

def displaycity():
    print("bangkok")
    displayFood()

displaycity()