n=input()
x=0 #한 자리수를 만들기 위해 몇 번 반복했는지

while len(n)>=2:
    sum=0 #자리수마다의 합
    for i in range(len(n)): 
        sum+=int(n[i]) #각 자리수를 합하기
    n=str(sum) #합한 숫자 문자열로 변경
    x+=1 #반복수 1 증가 
print(x) #x 출력

if int(n)%3==0: 
    print("YES") 
else:   
    print('NO')