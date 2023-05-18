# 백발백중
# import math => math.sqrt
import sys
input = sys.stdin.readline

x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

distance = ((x1-x2)**2 + (y1-y2)**2)

if distance >= (r1+r2)**2:
    print("NO")
else:
    print("YES")
