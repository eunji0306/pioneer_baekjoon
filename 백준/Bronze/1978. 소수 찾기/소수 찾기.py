#1978
n=int(input())
a=list(map(int,input().split()))
count=0

for i in a:
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            count+=1
print(count)