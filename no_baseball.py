from random import randint

def generate_numbers():
    numbers = []
    while len(numbers) < 3:
        new_ball_list = randint(0, 9)
        if new_ball_list not in numbers:
            numbers.append(new_ball_list)


    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다. \n")
    return numbers


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    # 코드를 작성하세요.
    while len(new_guess) < 3:
        new_guess_in = int(input("{}번째 숫자를 입력하세요:".format(len(new_guess)+1)))
        if new_guess_in in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요")
        elif new_guess_in > 9 or new_guess_in <0:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        else:
            new_guess.append(new_guess_in)

    return new_guess


def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0

    # 코드를 작성하세요.
    for i in range(3):
        if guesses[i] == solution[i]:
            strike_count += 1
        elif guesses[i] in solution and guesses[i] != solution[i]:
            ball_count += 1

    return strike_count, ball_count

# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

# 코드를 작성하세요.

while True:
    user_guess = take_guess()
    s, b = get_score(user_guess, ANSWER)

    print("{}S {}B\n".format(s, b))
    tries += 1

    if s == 3:
        break

#print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))







