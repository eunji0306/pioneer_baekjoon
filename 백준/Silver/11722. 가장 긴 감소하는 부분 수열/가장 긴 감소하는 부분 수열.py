#11722 - 뭐라는 걸까요 
n=int(input())
num=list(map(int, input().split()))

dp=[1]*n #가장 긴 감소하는 부분 수열의 길이 저장(최소 1)

for i in range(n):
    for j in range(i):
        if num[j]>num[i]:
            dp[i]=max(dp[i], dp[j]+1)

print(max(dp)) 