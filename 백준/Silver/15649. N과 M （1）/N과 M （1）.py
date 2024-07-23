#15649-과제
import sys
from itertools import permutations
n, m=map(int, input().split())
num=list(map(str, range(1, n+1))) #1부터 n까지의 숫자에 str 적용
map(str, range(1, n+1))
list(map(str, range(1, n+1)))
#이터러블 객체는 한 번에 한 개씩 값을 반환할 수 있는 데이터를 의미, 리스트, 튜플, 딕셔너리, 세트, 문자열, range 함수 등이 예
#permutations 함수의 첫 번째 인자는 선택할 수 있는 전체값, 두 번째 인자는 원하는 수열의 원소 개수
result='\n'.join(list(map(' '.join, permutations(num, m)))) #\n과 뒤 리스트를 합치기(변수에 저장 안 하면 줄바꿈이 안 되고 그냥 기호 그대로 출력됨. 왜지..?)
print(result) 