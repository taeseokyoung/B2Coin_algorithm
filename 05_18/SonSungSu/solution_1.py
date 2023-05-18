# https://www.acmicpc.net/problem/2438
#  백준 별찍기 1

def solution(n):
    if n <= 1:
        return n
    print("*" * solution(n - 1))
    return n

#  n == 5
# i = 5 , n = 5
# i = 4 , n = 4
# i = 3 , n = 3
# i = 2 , n = 2
# i = 1 , n = 1

# 재귀
# solution(int(input())+1)

# 반복문
# print("".join([f"{'*' * i}\n" for i in range(1, int(input()) + 1)]))

# 반복문 2
for i in range(1,int(input())+1):
    print("*"*i)

