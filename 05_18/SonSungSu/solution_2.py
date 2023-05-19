# 문제 링크 : https://www.acmicpc.net/problem/2753
#  문제 : 윤년

# 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때
# 4의 배수이면서 100의 배수가 아니라면 True
# 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다.
# 2000년은 400의 배수이기 때문에 윤년이다.


n = int(input())
print(1 if(n % 4 == 0 and  n % 100 != 0 or n % 400 == 0) else 0)
