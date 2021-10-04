n=int(input("Введите n: "))
check=False
rasst=[]
tarifs=[]
while not check:
    rasst=list(map(int, input("Введите n расстояний через пробел:\n").split()))
    if n == len(rasst):
        check=True
    else:
        print("Количество расстояний не совпадает с n")
check=False
while not check:
    tarifs=list(map(int,input("Введите n тарифов через пробел:\n").split()))
    if n == len(tarifs):
        check = True
    else:
        print("Количество тарифов не совпадает с n")

rasst_sorted=[]
tarifs_sorted=[]
for i in range(n):
    rasst_sorted.append((i,rasst[i]))
    tarifs_sorted.append((i,tarifs[i]))

rasst_sorted=sorted(rasst_sorted, key=lambda i: i[1])
tarifs_sorted=sorted(tarifs_sorted, key=lambda i: i[1], reverse=True)

out=[0]*n

for i in range(n):
    out[rasst_sorted[i][0]] = tarifs_sorted[i][0] + 1

for i in range(n):
    print(f"{i+1}-й сотрудник должен уехать на {out[i]}-й машине")
