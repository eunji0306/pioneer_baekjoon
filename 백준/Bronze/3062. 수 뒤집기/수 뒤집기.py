def solution(a):
  reva=int(str(a)[::-1])
  result=a+reva
  result=str(result)
  half=len(result)//2

  for i in range(half):
    if result[i]!=result[-(i+1)]:
      return 'NO'    
  return 'YES'
    
num=int(input())

for _ in range(num):
  x=int(input())
  print(solution(x))