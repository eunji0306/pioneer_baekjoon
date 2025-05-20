#1018
n, m=map(int, input().split()) #가로 세로 길이
board=[] #보드
result=[] #결과

for x in range(n):
    board.append(input()) #n줄만큼 1줄씩 입력받기

#8*8 보드
for i in range(n-7):
    for j in range(m-7):
        index1=0 #B로 시작하는 체스를 만들기 위해 다시 색칠해야 하는 칸의 수, 짝수가 B, 홀수가 W 
        index2=0 #W로 시작하는 체스를 만들기 위해 다시 색칠해야 하는 칸의 수, 짝수가 W, 홀수가 B
        
        #체스판은 가로 또는 세로로 인접한 칸은 반드시 색이 달라야 함
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b)%2==0: #(a+b)가 짝수
                    if board[a][b]!='B': #B가 아니면 
                        index1+=1 
                    if board[a][b]!='W': #W가 아니면
                        index2+=1 
                
                else: #(a+b)가 홀수
                    if board[a][b]!='W': #W가 아니면
                        index1+=1 
                    if board[a][b]!='B': #B가 아니면
                        index2+=1 
                        
        result.append(index1) #계산된 결과값 추가
        result.append(index2) # ''
        
print(min(result)) #최솟값 출력