# 소수 찾기

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))
# print(nums) -> [1, 3, 5, 7]
# nums = map(int,input().split()) -> map object

count = 0 
for num in nums:
    error = 0
    if num>1:
        for x in range(2,num):
            if num % x == 0:
                error = 1
        if error == 0:
            count+=1
                
print(count)