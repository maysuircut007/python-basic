fw = open("78.score.txt", "w", encoding = "utf-8")
fw.write("fuck you\n")
fw.write("baby")
fw.close()


fr = open("78.score.txt", "r", encoding = "utf-8")
#print(fr.read())

line = fr.readlines() # ภายในวงเล็บ จำนวน
for i in line:
    print("=>",i)


fa = open("78.score.txt", "a", encoding = "utf-8")
name = input("ใส่ชือของคุณ : ")
for x in range(5):
    fa.writelines(name+"\n")
fr.close()
fa.close()




