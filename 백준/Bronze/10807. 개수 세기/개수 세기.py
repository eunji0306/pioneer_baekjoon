#4단계-1차원 배열
#10807
num=int(input())
arr=list(map(int, input().split()))
a=int(input())
count=0

for i in range(num):
  if arr[i]==a:
    count+=1
print(count)