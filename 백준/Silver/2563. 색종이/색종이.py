#2563
n=int(input())
count=0
paper=[[0 for _ in range(100)] for _ in range(100)] #100x100 사이즈의 2차원 배열 생
for _ in range(n):
  a, b=map(int, input().split())
  for i in range(a, a+10): #가로 크기 10
    for j in range(b, b+10): #세로 크기 10
      paper[i][j]=1

for i in range(100): #위의 for문에서 count를 추가해버리면 중복된 부분도 같이 숫자가 세어짐->다시 for문
  for j in range(100):
    if paper[i][j]==1:
      count+=1
print(count)