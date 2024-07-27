#9656-과제
n=int(input())
a=[0]*1001 #0부터 1000까지의 인덱스를 저장

a[1]=1
a[2]=0
a[3]=1
a[4]=0

for i in range(5, n+1):
  if a[i-1]==0 or a[i-3]==0:
    a[i]=1
  else:
    a[i]=0
  
if a[n]==1:
  print("CY")
else:
  print("SK")