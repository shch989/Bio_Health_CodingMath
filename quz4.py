# 문제 4 (30점) - 딕셔너리 사용
# 아래 질병 코드를 딕셔너리로 만들고 화면에 출력하기
# k20": "식도염, k21": "위 식도역류병, k22": "식도의 기타 질환, k23*": "달리 분류된 질환에서의 식도의 장애
# k25": "위궤양, k26": "십이지장궤양, k27": "상세불명 부위의 소화성 궤양, k28": "위공장궤양
# k29": "위염 및 십이지장염, k30": "기능성 소화불량, k31": "위 및 십이지장의 기타 질환
# 사용자로부터 5명의 환자 이름과 아래 질병 코드 한개를 차례대로 입력 받아 딕셔너리에 저장하기 (단, 동일 질병 2인 이상 입력)
# 사용자에게 환자 이름 입력 받아 해당 환자의 질병을 조회하여 화면에 환자이름과 질병코드, 질병명을 출력하기
# 사용자에게 질병 코드를 입력 받아 해당 질병의 환자 이름과 질병 코드, 질병명을 화면에 출력하기 (단, 동일 질병 2인 이상 출력 가능)

# 질병 코드 딕셔너리 만들기
disease_dict = {
    "k20": "식도염",
    "k21": "위 식도역류병",
    "k22": "식도의 기타 질환",
    "k23*": "달리 분류된 질환에서의 식도의 장애",
    "k25": "위궤양",
    "k26": "십이지장궤양",
    "k27": "상세불명 부위의 소화성 궤양",
    "k28": "위공장궤양",
    "k29": "위염 및 십이지장염",
    "k30": "기능성 소화불량",
    "k31": "위 및 십이지장의 기타 질환"
}

# 환자 정보 딕셔너리 만들기
patient_dict = {}
for i in range(5):
    name = input("환자 이름 입력: ")
    disease_code = input("질병 코드 입력: ")
    patient_dict[name] = disease_code

# 사용자에게 질병 조회 및 출력
while True:
    name = input("조회할 환자 이름 입력 (종료는 'exit'): ")
    if name == "exit":
        break
    disease_code = patient_dict.get(name)
    if disease_code:
        disease_name = disease_dict.get(disease_code)
        print(f"{name}: {disease_code} ({disease_name})")
    else:
        print("등록되지 않은 환자입니다.")

# 사용자에게 환자 조회 및 출력
while True:
    disease_code = input("조회할 질병 코드 입력 (종료는 'exit'): ")
    if disease_code == "exit":
        break
    patient_list = []
    for name, code in patient_dict.items():
        if code == disease_code:
            patient_list.append(name)
    if patient_list:
        disease_name = disease_dict.get(disease_code)
        patient_str = ", ".join(patient_list)
        print(f"{disease_code} ({disease_name}): {patient_str}")
    else:
        print("등록된 환자가 없습니다.")
