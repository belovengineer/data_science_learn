import numpy as np

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    first = 0
    last = 101
    
    while True:
        count +=1
        predict_number = (last + first) // 2 # выражение, применяемое в условиях, присваиваем predict_number
        if number < predict_number:
            first = predict_number
        elif number > predict_number:
            first = predict_number
        else:
            break
        
    return count

print('Hello')
print(random_predict())