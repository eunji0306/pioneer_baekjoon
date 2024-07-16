#백준 5597
b=[]
for _ in range(28):
  a=int(input())
  b.append(a)

for i in range(1, 31):
  if i not in b:
    print(i)