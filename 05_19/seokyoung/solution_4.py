num1 = input()
# 4

num_list = list(map(int, input().split()))
# 1 3 5 7

answer = []
for i in num_list: # num에 입력받은 숫자를 하나씩
        # i = 1 3 5 7 이 순서대로 들어온다.
        
    for n in range(i,1,-1): #1 ,123, 12345, 1234567
        j = 2
        if i % n > 0:
            
            j += 1
        print(n, i)
        # if count == 0:
        #     answer.append(n)
        # if i % n == 0:
        #     count += 1

    print(answer) # 받은 값 중 소수의 갯수만 프린트