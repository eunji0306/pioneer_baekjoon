#24416-과제
def fib(n):
  a=[0]*41
  a[1]=1
  a[2]=1
  for i in range(3, n+1):
    a[i]=a[i-1]+a[i-2]
  return a[n]
  
def fibo(n):
  return n-2

n=int(input())
print(fib(n), fibo(n))