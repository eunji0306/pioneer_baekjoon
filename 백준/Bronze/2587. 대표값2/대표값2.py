#2587
b=[]
temp=0

for _ in range(5):
  a=int(input())
  b.append(a)
for i in range(0, len(b), 1):
  for j in range(0, len(b)-i-1, 1):
    if b[j]>b[j+1]:
      temp=b[j]
      b[j]=b[j+1]
      b[j+1]=temp

print(sum(b)//5)
print(b[2])