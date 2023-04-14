# 문제 1 (20점) - 리스트, numpy 사용
# 사용자로부터 100이하의 정수 5개를 입력 받아 리스트로 저장하고
# 컴퓨터가 무작위로 100이하의 정수 5개를 생성하여 리스트로 저장하고
# 각각 사용자와 컴퓨터가 입력 받은 값의 총합, 평균, 분산, 표준편차를 계산하여 화면에 출력하기
# - import random
# - import numpy


import random
import numpy as np

# 사용자로부터 100이하의 정수 5개를 입력 받아 리스트로 저장
user_nums = []
for i in range(5):
    num = int(input("100 이하의 정수를 입력하세요: "))
    user_nums.append(num)

# 컴퓨터가 무작위로 100이하의 정수 5개를 생성하여 리스트로 저장
comp_nums = [random.randint(1, 100) for i in range(5)]

# 각각 사용자와 컴퓨터가 입력 받은 값의 총합, 평균, 분산, 표준편차 계산
user_total = sum(user_nums)
user_mean = np.mean(user_nums)
user_var = np.var(user_nums)
user_std = np.std(user_nums)

comp_total = sum(comp_nums)
comp_mean = np.mean(comp_nums)
comp_var = np.var(comp_nums)
comp_std = np.std(comp_nums)

# 결과 출력
print("사용자가 입력한 값:", user_nums)
print("컴퓨터가 생성한 값:", comp_nums)
print("사용자가 입력한 값의 총합:", user_total)
print("컴퓨터가 생성한 값의 총합:", comp_total)
print("사용자가 입력한 값의 평균:", user_mean)
print("컴퓨터가 생성한 값의 평균:", comp_mean)
print("사용자가 입력한 값의 분산:", user_var)
print("컴퓨터가 생성한 값의 분산:", comp_var)
print("사용자가 입력한 값의 표준편차:", user_std)
print("컴퓨터가 생성한 값의 표준편차:", comp_std)
