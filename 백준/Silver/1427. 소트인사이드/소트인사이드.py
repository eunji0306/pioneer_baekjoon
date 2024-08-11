#1427
a=list(input())
temp=0

for i in range(0, len(a)):
  max=i
  for j in range(i+1, len(a), 1):
    if a[max]<a[j]:
      max=j
  temp=a[i]
  a[i]=a[max]
  a[max]=temp

for i in a:
  print(i, end='')