#백준 1546
n=int(input())
a=list(map(int, input().split()))
sum=0

M=max(a)
a.sort()
for i in range(n):
    a[i] = a[i]/M*100
    sum+=a[i]
result=sum/n
print(result)