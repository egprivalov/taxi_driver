n=int(input("Введите n: "))
check=False
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

rasst_sorted=sorted(rasst)
tarifs_sorted=sorted(tarifs, reverse=True)

out=[0]*n

for i in range(n):
    out[rasst.index(rasst_sorted[i])]=tarifs.index(tarifs_sorted[i])+1

for i in range(n):
    print(f"{i+1}-й сотрудник должен уехать на {out[i]}-й машине")
