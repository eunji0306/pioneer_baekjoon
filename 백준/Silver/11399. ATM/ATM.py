#11399
n=int(input())
lst=list(map(int, input().split()))
temp=0
answer=0

for i in range(0, len(lst), 1):
  for j in range(i, 0, -1):
    if lst[j]<lst[j-1]:
      temp=lst[j]
      lst[j]=lst[j-1]
      lst[j-1]=temp
      
for _ in range(1, n+1):
  answer+=sum(lst[:_])
print(answer)