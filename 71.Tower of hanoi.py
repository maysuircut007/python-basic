

def tower_of_hanoi(n, a, b, c):
    if n == 0:
        return
    tower_of_hanoi(n-1, a, c, b)
    print("จานที่ ", n, "จาก ", a, "ไป ",c  )
    tower_of_hanoi(n-1, b, a, c,) 


tower_of_hanoi(5, "A", "B", "C")