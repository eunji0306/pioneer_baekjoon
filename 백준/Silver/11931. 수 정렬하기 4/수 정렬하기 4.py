#11931-선택정렬로 하니까 시간초과로 안 돼서(PyPy3 써도 안 돼요..) 일단 sort 써서 제출하고 주석으로 선택정렬 코드 제출합니당.. 
#sort 사용
a=int(input())
lst=[]

for _ in range(a):
  num=int(input())
  lst.append(num)

lst.sort(reverse=True)

for i in range(0, len(lst), 1):
  print(lst[i])

#아래가 선택정렬 코드
'''
a=int(input())
lst=[]
temp=0

for _ in range(a):
  num=int(input())
  lst.append(num)

for i in range(0, len(lst)):
  min=i
  for j in range(i+1, len(lst), 1):
    if lst[min]<lst[j]:
      min=j
  temp=lst[i]
  lst[i]=lst[min]
  lst[min]=temp

for i in range(0, len(lst), 1):
  print(lst[i])
  '''