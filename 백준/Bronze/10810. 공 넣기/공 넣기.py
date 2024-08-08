#10810
a, b=map(int, input().split())
basket=[0]*100

for i in range(b):
  c, d, e=map(int, input().split())
  for j in range(c, d+1):
    basket[j-1]=e

for x in range(a):
  print(basket[x], end=" ")