"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    predict_number = np.random.randint(1, 101)  # предполагаемое число
    count = 0
    low = 1  # присваиваем значение, соответствующее нижней границе диапазона поиска
    high = 101  # присваиваем значение, соответствующее верхней границе диапазона поиска +1
    while True:
        mid = (high+low)//2
        count += 1
        if mid == predict_number:
            break  # выход из цикла если угадали
        elif predict_number > mid:
            low = mid  # перезаписываем переменную low
        else:
            high = mid # перезаписываем переменную high
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
