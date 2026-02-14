"""Игра «Угадай число» (улучшенная версия)
Компьютер загадывает и угадывает число с помощью бинарного поиска.
"""

import numpy as np

def binary_predict(number: int = 1) -> int:
    """Угадывает число методом бинарного поиска

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    low = 1
    high = 100

    while low <= high:
        count += 1
        mid = (low + high) // 2

        if mid == number:
            return count
        elif mid < number:
            low = mid + 1
        else:
            high = mid - 1

    return count  # на всякий случай


def score_game(predict_function) -> int:
    """Оценивает среднее количество попыток за 1000 раундов

    Args:
        predict_function: функция угадывания

    Returns:
        int: среднее количество попыток
    """
    np.random.seed(1)  # фиксируем для воспроизводимости
    random_array = np.random.randint(1, 101, size=1000)

    attempts = []
    for number in random_array:
        attempts.append(predict_function(number))

    score = int(np.mean(attempts))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


# Запуск
if __name__ == "__main__":
    score_game(binary_predict)