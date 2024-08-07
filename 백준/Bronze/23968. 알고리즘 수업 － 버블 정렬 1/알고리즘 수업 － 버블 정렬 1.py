#23968
a, b=map(int, input().split())
c=list(map(int, input().split()))
cnt=0

def bubble(c):
  global cnt #함수 내부에서 값을 수정하기 위해서는 전역 변수임을 설정해 줘야 한다네요..
  for i in range(0, len(c), 1):
    for j in range(0, len(c)-i-1, 1):
      if c[j]>c[j+1]:
        temp=c[j]
        c[j]=c[j+1]
        c[j+1]=temp
        cnt+=1
        if cnt==b:
          return(c[j], c[j+1])
  return(-1)

result=bubble(c)
if result==-1:
    print(result)
else:
    print(result[0], result[1]) #각각 c[j]와 c[j+1]을 의미