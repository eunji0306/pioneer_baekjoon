#25305
a, b=map(int, input().split())
c=list(map(int, input().split()))

for i in range(0, len(c), 1):
  for j in range(0, len(c)-i-1, 1):
    if c[j]<c[j+1]:
      temp=c[j]
      c[j]=c[j+1]
      c[j+1]=temp
print(c[b-1])