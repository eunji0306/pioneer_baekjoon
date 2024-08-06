#10871
num, a=map(int, input().split())
arr=list(map(int, input().split()))

for i in range(num):
  if arr[i]<a:
    print(arr[i], end=" ")