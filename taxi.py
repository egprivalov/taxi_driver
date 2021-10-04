n=int(input("Введите n: "))
rasst=list(map(int, input("Введите n расстояний через пробел:\n").split()))
tarifs=list(map(int,input("Введите n тарифов через пробел:\n").split()))

rasst_sorted=sorted(rasst)
tarifs_sorted=sorted(tarifs, reverse=True)

out=[0]*n

for i in range(n):
    out[rasst.index(rasst_sorted[i])]=tarifs.index(tarifs_sorted[i])+1

print(*out)
