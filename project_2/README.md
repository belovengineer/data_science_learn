# Проект 2. Прогнозирование рейтинга отеля на Booking

![avatar](https://www.pataradardanoshotel.com/wp-content/uploads/2016/04/booking_logo_blu.png)

## Оглавление  
[1. Описание проекта](https://github.com/belovengineer/data_science_learn/tree/main/project_3/README.md#Описание-проекта)  
[2. Какой кейс решаем?](https://github.com/belovengineer/data_science_learn/tree/main/project_3/README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](https://github.com/belovengineer/data_science_learn/tree/main/project_3/README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](https://github.com/belovengineer/data_science_learn/tree/main/project_3/README.md#Этапы-работы-над-проектом)  
[5. Результат](https://github.com/belovengineer/data_science_learn/tree/main/project_3/README.md#Результат)    
[6. Выводы](https://github.com/belovengineer/data_science_learn/tree/main/project_3/README.md#Выводы) 

### Описание проекта    
  
Создаем модель предсказания рейтинга отелей для нахождения накрученных отзывов.

<b>Стэк-технологии:</b>
* Математические функции и статистика - NumPy, Statistics   
* Обработка и анализ данных - Pandas  
* Визуализация данных - Matplotlib, Seaborn, Plotly  
* Машинное обучение - Scikit-learn
* Обработка естественного языка - Natural Language Toolkit
  
:arrow_up:[к оглавлению](https://github.com/belovengineer/data_science_learn/tree/main/project_2/README.md#Оглавление)


### Какой кейс решаем?  
  
Вы работаете датасаентистом в компании Booking. Одна из проблем компании — это нечестные отели, которые накручивают себе рейтинг. Одним из способов нахождения таких отелей является построение модели, которая предсказывает рейтинг отеля. Если предсказания модели сильно отличаются от фактического результата, то, возможно, отель играет нечестно, и его стоит проверить.
  
Вам поставлена задача создать такую модель.
  
Делаем реальный ML продукт, который потом сможет нормально работать на новых данных.
  
### Краткая информация о данных
  
<b>В качестве данных принимаем:</b>
* hotels_train.csv - набор данных для обучения  
* hotels_test.csv - набор данных для оценки качества  
* submission.csv - файл сабмишна в нужном формате  
  
<b>Признаки:</b>  
* hotel_address - адрес отеля  
* review_date - дата, когда рецензент разместил соответствующий отзыв.  
* average_score - средний балл отеля, рассчитанный на основе последнего комментария за последний год  
* hotel_name - название отеля  
* reviewer_nationality - национальность рецензента  
* negative_review - отрицательный отзыв, который рецензент дал отелю.  
* review_total_negative_word_counts - общее количество слов в отрицательном отзыв  
* positive_review - положительный отзыв, который рецензент дал отелю  
* review_total_positive_word_counts - общее количество слов в положительном отзыве  
* reviewer_score - оценка, которую рецензент поставил отелю на основе своего опыта  
* total_number_of_reviews_reviewer_has_given - количество отзывов, которые рецензенты дали в прошлом  
* total_number_of_reviews - общее количество действительных отзывов об отеле  
* tags - теги, которые рецензент дал отелю.  
* days_since_review - продолжительность между датой проверки и датой очистки  
* additional_number_of_scoring - есть также некоторые гости, которые просто поставили оценку сервису, а не оставили отзыв. Это число указывает, сколько там действительных оценок без проверки.  
* lat - широта отеля  
* lng - долгота отеля  
  
:arrow_up:[к оглавлению](https://github.com/belovengineer/data_science_learn/tree/main/project_2/README.md#Оглавление)


### Этапы работы над проектом  
1. Подгрузка и предварительный анализ данных 
2. Очистка данных: на этом этапе корректируем признак "hotel_name". Находим отели с одинаковыми названиями, но разными адресами и меняем названия.  
3. Обработка признаков  
    3.1. Признак "hotel_address" - создаём новые признаки города и страны, в которой находится отель. Удаляем адрес и кодируем город отеля.  
    3.2. Признаки страна рецензента и соответствие страны рецензента стране отеля - создаём признак соответствия, кодируем признак национальности. Удаляем город и страну отеля, признак национальности.  
    3.3. Признак даты отзыва - выделяем месяц, когда был написан отзыв. Кодируем признак в высокий или низкий сезон.  
    3.4. Создаем и кодируем признак срока давности отзыва. Удаляю признак даты отзыва.  
    3.5. Признак Отрицательный отзыв.  
    3.6. Признак Процент истиных негативных отзывов по каждому отелю. Удаляем признак количества отзывов и количества негативных отзывов.  
    3.7. Признак Положительный отзыв.  
    3.8. Признак Процент истиных полоэительных отзывов.  
    3.9. Признак процентного содержания негативных и позитивных слов в отзыве.  
    3.10. Признак разности количества слов в положительном и отрицательнос отзывах.  
    3.11. Признак удовлетворенности рецензента отелем. Удаляю признаки отзывов.    
    3.12. Признак Tags. Кодирую 30 популярных тегов.   
4. Подготовка данных к обучению модели  
    4.1. Удаляем признаки типа object  
    4.2. Проверяем признаки на мультиколлинеарность  
    4.3. Удаляю сильно коррелирующие и неинформативные признаки  
    4.4. Стандартизирую признаки средней оценки и количества слов позитивного отзыва  
    4.5. Проверяем признаки значимости  
4. Обучение модели и анализ результатов  

:arrow_up:[к оглавлению](https://github.com/belovengineer/data_science_learn/tree/main/project_2/README.md#Оглавление)


### Результаты:  
Результат работы проекта - игра, в которой компьютер, благодаря применению бинарного поиска, угадывает загаданное число в среднем менее чем за 20 раз. В нашем случае, алгоритм угадывает число менее чем за 8 попыток.

:arrow_up:[к оглавлению](https://github.com/belovengineer/data_science_learn/tree/main/project_2/README.md#Оглавление)


### Выводы:  
В ходе работы над задачей применен самый эффективный алгоритм решения. Дальнейшие попытки уменьшить количество попыток не увенчались успехом (не смотря на то, что для данной задачи это уже было бы излишне).

:arrow_up:[к оглавлению](https://github.com/belovengineer/data_science_learn/tree/main/project_2/README.md#Оглавление)


Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами
