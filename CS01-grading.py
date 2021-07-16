A = int(input("1:"))
B = int(input("2:"))
C = int(input("3:"))
point = A + B + C
if 100 >= point >= 80:
    print("A")
elif 80 > point >= 75:
    print("B+")
elif 75 > point >= 70:
    print("B")
elif 70 > point >= 65:
    print("C+")
elif 65 > point >= 60:
    print("C")
elif 60 > point >= 55:
    print("D+")
elif 55 > point >= 50:
    print("D")
elif 50 > point >= 0:
    print("F")
else: print('something went worng')     

    