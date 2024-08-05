#2750
a=int(input())
b=[]
temp=0

for i in range(a):
  b.append(int(input()))

for i in range(0, len(b), 1):
  for j in range(0, len(b)-i-1, 1):
    if b[j]>b[j+1]:
      temp=b[j]
      b[j]=b[j+1]
      b[j+1]=temp

for _ in range(0, len(b), 1):
  print(b[_])