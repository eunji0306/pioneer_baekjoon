#10818
num=int(input())
arr=list(map(int, input().split()))
arr.sort()
print(arr[0],arr[num-1])