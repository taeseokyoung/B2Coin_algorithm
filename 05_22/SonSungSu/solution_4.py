# https://www.acmicpc.net/problem/1978
# 문제 : 소수 찾기

def solution(x):
    if x < 2:
        return False

    for i in range(2,x):
        if x%i == 0:
            return False
        # elif (i+1)*(i+1) > x+1:
        elif i * i > x + 1:
            return True
    return True








# n = int(input())
# x = list(map(int,input().split()))
n = 20
cnt = 0

for i in range(1,n):
    # if solution(x[i]): # 제출용 코드
    if solution(i): # 테스트용 코드
        cnt +=1
print(cnt)
