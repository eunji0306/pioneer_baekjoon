#3052
arr=[]

for i in range(10):
  num=int(input())
  arr.append(num%42)

print(len(set(arr))) #set 함수는 중복 제거