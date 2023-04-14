# 문제 3 (25점) - 조건문, 반복문 사용
# 사용자로부터 이름, 성별(남자, 여자), 허리둘래(cm), 엉덩이 둘레(cm),
# 신장(cm), 체중(kg) 을 입력받아서 리스트에 저장하고 각각 WHP, BMI 값을 계산하여
# 사용자의 성별에 따른 비만 여부와 BMI 계산값을 화면에 출력하기
# - WHP(Wrist Hip Ratio): 허리둘레(cm) / 엉덩이둘레 (cm)
#  - 남자: WHP > 0.9 이상이면 비만, 여자: WHP > 0.85 이상이면 비만
# - BMI = (체중 / (신장(m)^2))
#  - BMI가 0~19.9 이하이면 재측정
#  - BMI가 20~24.9 사이이면 정상
#  - BMI가 25~29.9 사이이면 과체중
#  - BMI가 30 이상이면 비만


name = input("이름을 입력하세요: ")
gender = input("성별을 입력하세요 (남자/여자): ")
waist = float(input("허리둘레(cm)를 입력하세요: "))
hip = float(input("엉덩이둘레(cm)를 입력하세요: "))
height = float(input("신장(cm)을 입력하세요: "))
weight = float(input("체중(kg)을 입력하세요: "))

whp = waist / hip
bmi = weight / ((height / 100) ** 2)

print("===== 분석 결과 =====")
print(f"이름: {name}")
print(f"성별: {gender}")

if gender == "남자":
    if whp >= 0.9:
        print("비만입니다.")
    else:
        print("비만이 아닙니다.")
elif gender == "여자":
    if whp >= 0.85:
        print("비만입니다.")
    else:
        print("비만이 아닙니다.")
else:
    print("잘못된 성별 입력입니다.")

print(f"BMI: {bmi:.1f}")

if bmi <= 19.9:
    print("저체중입니다. 재측정이 필요합니다.")
elif bmi <= 24.9:
    print("정상입니다.")
elif bmi <= 29.9:
    print("과체중입니다.")
else:
    print("비만입니다.")
