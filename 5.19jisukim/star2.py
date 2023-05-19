# 백준 별찍기2

# sol1 그냥 풀어보기
import sys
input = sys.stdin.readline
n = int(input())
for i in range(1,n+1):
    print(' '*(n-i)+'*'*i)

# sol2 오른쪽 정렬
for i in range(n):
    star = '*'*(i+1)
    print(star.rjust(n))
    # 전체 n에서 오른쪽 정렬을 하는 .rjust(n) 사용

# 재귀