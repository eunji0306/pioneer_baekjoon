#3085
n=int(input()) #보드 크기
candy=[list(input()) for x in range(n)] #사탕 색
result=0 #상근이가 먹을 수 있는 사탕의 최대 개수

def bomboni():
    global result
    
    for i in range(n): #가로 max 개수
        cnt=1
        for j in range(n-1):
            if candy[i][j] == candy[i][j+1]:
                cnt+=1
                result=max(result, cnt)
            else:
                cnt=1
            
    for i in range(n): #세로 max 개수
        cnt=1
        for j in range(n-1):
            if candy[j][i]==candy[j+1][i]:
                cnt+=1
                result=max(result, cnt)
            else:
                cnt=1
                
for i in range(n):
    for j in range(n-1):
        candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j] #가로 위치 바꿈
        bomboni()
        candy[i][j+1], candy[i][j] = candy[i][j], candy[i][j+1] #원상 복구
        
        candy[j][i], candy[j+1][i] = candy[j+1][i], candy[j][i] #세로 위치 바꿈
        bomboni()
        candy[j+1][i], candy[j][i] = candy[j][i], candy[j+1][i] #원상 복구
        
print(result)