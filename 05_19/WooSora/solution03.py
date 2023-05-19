
n = int(input()) # 대회 상금의 금액을 입력받음

total01 = n * 0.78                # n의 22%를 제외한 금액을 계산
total02 = (n * 0.8 ) + (n * 0.2 * 0.78 ) # 상금의 80%와 20% 중 78%를 계산

print(int(total01), int(total02)) # 실제 수령액을 출력
