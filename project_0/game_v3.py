"""Игра угадай число V3.0
    Компьютер сам загадывает и сам
        отгадывает число за 
        минимальное число попыток"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    minimum = 1
    maximum = 101
    predict_number = maximum // 2 #Предполагаемое число


    while number != predict_number: #Цикл определяющий количество попыток
        count+= 1
        if number > predict_number:
            minimum = predict_number
            predict_number = (minimum+maximum) // 2
        elif number < predict_number:
            maximum = predict_number
            predict_number = (minimum+maximum) // 2
    return(count) 
    
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов 
    угадывает наш алгоритм

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_list = [] #Список для сохранения количества попыток
    np.random.seed(1) #Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) #загадали список чисел

    for number in random_array:
        count_list.append(random_predict(number))
        
    score = int(np.mean(count_list)) #Находим среднее количество попыток
    min_score = int(np.min(count_list)) #Находим минимальное количество попыток
    max_score = int(np.max(count_list)) #Находим максимальное количество попыток
    
    if min_score == 0: #Если минимальное количество попыток 0, корректируем результаты
        score += 1
        min_score += 1
        max_score += 1
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток \n'
          f'Максимальное количество попыток {max_score}. Минимальное количество попыток {min_score}'
          )
    return(score, max_score, min_score)

#RUN
if __name__ == '__main__':
    score_game(random_predict)