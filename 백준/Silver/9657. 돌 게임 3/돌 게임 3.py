#9657-과제
n=int(input())
a=[0]*1001

a[1]=1
a[2]=0
a[3]=1
a[4]=1

for i in range(5, n+1):
  if a[i-1]==0 or a[i-3]==0 or a[i-4]==0:
    a[i]=1
  else:
    a[i]=0
    
if a[n]==1:
  print("SK")
else:
  print("CY")