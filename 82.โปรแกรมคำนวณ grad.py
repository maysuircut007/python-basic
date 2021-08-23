
fw = open("81.score.txt", "w", encoding = "utf-8")
try:
    while True:
        studentid = input("ป้อนรหัสผ่าน")
        if studentid == "Exit":
            break
        score = input("ป้อนคะเเนน")
        fw.writelines(studentid + "\t" + score + "\n")
    fw.close()
    fr = open("81.score.txt", "r", encoding = "utf-8")
    fg = open("83.grad.txt", "w", encoding = "utf-8")
    for line in fr.readlines():
        score = line[-4:].strip()   
        studentid = line[:-4].strip()  
        score = int(score)
        
        if score >= 80:
            grad = "A"
        elif score >= 70 and score < 80:
            grad = "B"
        elif score >= 50 and score < 70:
            grad = "C"
        else:
            grad = "f"
        print("รหัส = ", studentid, "คะเเนน", score, "เกรด", grad)
        fg.writelines(studentid + "\t" + str(score) + "\t" + grad + "\n")
    fg.close()


except Exception as e:
    print(e)
