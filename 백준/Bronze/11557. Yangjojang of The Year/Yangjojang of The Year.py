a=int(input())
for i in range(a):
  school=[]
  soju=[]
  n=int(input())
  for j in range(n):
    a, b=input().split()
    school.append(a)
    soju.append(int(b))
  maxsoju=soju.index(max(soju))
  print(school[maxsoju])