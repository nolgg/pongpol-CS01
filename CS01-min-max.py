Num = int(input('Enter loop numbers:'))
Numtotal = []
for i in range(Num):
    data = int(input('Enter data:'))
    Numtotal += [data]
Numtotal.sort(reverse=False)
print("min :",Numtotal[0])
nvm = len(Numtotal)
print("max :",Numtotal[nvm-1])