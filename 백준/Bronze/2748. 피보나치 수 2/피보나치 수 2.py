#2748
n=int(input())

fibo=[0]*(n+1)
fibo[1]=1

for i in range(2, n+1):
    fibo[i]=fibo[i-2]+fibo[i-1]

print(fibo[n])