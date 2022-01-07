import random

# 코드를 작성하세요.
ran = random.randint(1, 20)
chance = 4

while chance > 0:
    val = int(input("기회가 {}번 남았습니다. 1 - 20 사이의 숫자를 맞혀 보세요 : ".format(chance)))
    if val == ran:
        print("축하합니다.{}번 만에 숫자를 맞히셨습니다.".format(chance))
        break
    elif val > ran:
        chance -= 1
        print("DOWN")
    elif val < ran:
        chance -= 1
        print("UP")
    else:
        print("올바른 값이 아닙니다. 숫자를 적어 주세요")
    if chance == 0:
        print("정답을 맞추지 못했어요. 정답은 {}입니다.".format(ran))
