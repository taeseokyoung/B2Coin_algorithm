N = int(input())

if N % 4 or (N % 100 == 0 and N % 400):
    print(0)
else:
    print(1)