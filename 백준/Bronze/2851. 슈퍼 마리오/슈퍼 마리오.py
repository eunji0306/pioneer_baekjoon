#2851-과제
a=[]
score=0

for _ in range(10):
  a.append(int(input()))

for i in a:
  score+=i
  if score>=100:
    if score-100>100-(score-i): #score-a[_]는 전 단계
      score-=i #더 작은 수가 100에서 가까운 것이므로 우항 거가 최종 점수
    break
print(score)