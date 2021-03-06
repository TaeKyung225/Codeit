# 화씨 온도에서 섭씨 온도로 바꿔 주는 함수
def fahrenheit_to_celsius(fahrenheit):
    # 코드를 입력하세요.
    return (fahrenheit - 32) * 5 / 9


temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: " + str(temperature_list))  # 화씨 온도 출력

# 리스트의 값들을 화씨에서 섭씨로 변환하는 코드를 입력하세요.

n = len(temperature_list)
b = 0

while b < n:
    temperature_list[b] = round(fahrenheit_to_celsius(temperature_list[b]), 1)
    b += 1

print("섭씨 온도 리스트: {}".format(temperature_list))  # 섭씨 온도 출력
print(n)