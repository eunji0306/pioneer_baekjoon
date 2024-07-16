#백준 16435
n, l=map(int, input().split())
a=list(map(int, input().split()))
a.sort()

for i in range(len(a)):
  if a[i]<=l:
    l+=1
  else:
    break
print(l)