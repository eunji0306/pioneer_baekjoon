#1427
a=list(input())
temp=0

for i in range(0, len(a)):
  min=i
  for j in range(i+1, len(a), 1):
    if a[min]<a[j]:
      min=j
  temp=a[i]
  a[i]=a[min]
  a[min]=temp

for i in a:
  print(i, end='')