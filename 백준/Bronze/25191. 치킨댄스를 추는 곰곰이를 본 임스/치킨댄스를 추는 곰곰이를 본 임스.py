#백준 25191
n=int(input())
a, b=map(int, input().split())
result=0

if n>a/2+b and a%2==0:
  result=a/2+b
elif n>a/2+b and a%2!=0:
  result=(a-1)/2+b
else:
  result=n
print(int(result))