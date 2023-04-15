# 문제 1 (20점) - 리스트, numpy 사용
# 사용자로부터 100이하의 정수 5개를 입력 받아 리스트로 저장하고
# 컴퓨터가 무작위로 100이하의 정수 5개를 생성하여 리스트로 저장하고
# 각각 사용자와 컴퓨터가 입력 받은 값의 총합, 평균, 분산, 표준편차를 계산하여 화면에 출력하기
# - import random
# - import numpy


import random
import numpy as np

# 사용자로부터 100이하의 정수 5개를 입력 받아 리스트로 저장
A = []
for i in range(5):
    num = int(input("100 이하의 정수를 입력하세요: "))
    A.append(num)

# 컴퓨터가 무작위로 100이하의 정수 5개를 생성하여 리스트로 저장
B = [random.randint(1, 100) for i in range(5)]

# 각각 사용자와 컴퓨터가 입력 받은 값의 총합, 평균, 분산, 표준편차 계산
A_sum = np.sum(A)
A_average = np.average(A)
A_var = np.var(A)
A_std = np.std(A)

B_sum = np.sum(B)
B_average = np.average(B)
B_var = np.var(B)
B_std = np.std(B)

# 결과 출력
print("사용자가 입력한 값:", A)
print("컴퓨터가 생성한 값:", B)
print("사용자가 입력한 값의 총합:", A_sum)
print("컴퓨터가 생성한 값의 총합:", B_sum)
print("사용자가 입력한 값의 평균:", A_average)
print("컴퓨터가 생성한 값의 평균:", B_average)
print("사용자가 입력한 값의 분산:", A_var)
print("컴퓨터가 생성한 값의 분산:", B_var)
print("사용자가 입력한 값의 표준편차:", A_std)
print("컴퓨터가 생성한 값의 표준편차:", B_std)
