#백준 1934
import math
n=int(input())
result=0
for i in range(n):
  a, b=map(int, input().split())

  if a==0 or b==0:
    result=0
  else:
    result=a*b/math.gcd(a, b)
  print(int(result))