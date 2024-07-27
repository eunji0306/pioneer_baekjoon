#9655-과제
n=int(input())
a=[0]*1001 #0부터 1000까지의 인덱스를 저장

a[1]=1
a[2]=0
a[3]=1
a[4]=0

#동적 계획법 설립
for i in range(5, n+1):
  if a[i-1]==0 or a[i-3]==0: #a[2]가 0이기 때문에 a[i-3]==0일 때도 같이 추가
    a[i]=1
  else: #0이 아니면
    a[i]=0
  
if a[n]==1:
  print("SK")
else:
  print("CY")