#2579
n=int(input())

s=[0]*301

for i in range(1, n+1):
    s[i]=int(input())

dp=[0]*301

dp[0]=s[0]
dp[1]=s[0]+s[1]
dp[2]=max(s[0]+s[2], s[1]+s[2])

for i in range(3, n+1):
    dp[i]=max(s[i]+s[i-1]+dp[i-3], s[i]+dp[i-2])

print(dp[n])