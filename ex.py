import random
vacab = {}
with open('vocabulary.txt', 'r', encoding="UTF-8") as f:
    for line in f:
        data = line.strip().split(": ")
        english_word, korean_word = data[0], data[1]
        vacab[english_word] = korean_word

        keys = list(vacab.keys())
        index = random.randint(0, len(keys) - 1)
        english_word = keys[index]
        korean_word = vacab[english_word]

        guess = input("{}: ".format(korean_word))
        if guess == english_word:
            print("맞았습니다!")
        elif guess == "q":
             break
        else:
             print("아쉽습니다. 정답은 {}입니다.".format(english_word))
