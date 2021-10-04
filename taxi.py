n=int(input())
rasst=list(map(int, input().split()))
tarifs=list(map(int,input().split()))

rasst_sorted=sorted(rasst)
tarifs_sorted=sorted(tarifs, reverse=True)

out=[0]*n

for i in range(n):
    out[rasst.index(rasst_sorted[i])]=tarifs.index(tarifs_sorted[i])+1

print(*out)