# for i in range(1, int(input())+1):
#     print(i*'*')
# print(dir(str))
# print(type(rjust()))

N = int(input())
for i in range(1, N+1):
    # 1
    #   print((' ' * (N-i)) + (i * '*'))

    # 2
    i = i*'*'
    print(i.rjust(N))
