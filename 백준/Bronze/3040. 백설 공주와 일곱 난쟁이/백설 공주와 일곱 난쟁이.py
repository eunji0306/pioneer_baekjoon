#백준 3040
b=[]
for _ in range(9):
  a=int(input())
  b.append(a)

total=sum(b)
diff=total-100

for i in range(9):
    for j in range(i+1, 9):
      if b[i]+b[j]==diff:
        b.remove(b[i])
        b.remove(b[j-1])
        break
    if len(b)==7:
      break

for k in b:
  print(k)