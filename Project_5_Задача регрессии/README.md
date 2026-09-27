<center> <img src = https://www.autoblog.com/.image/NzowMDAwMDAwMDAxMTEyNzkw/photo-of-taxi-and-new-york-taxi-and-new-york-city-and-new-york-skyline.jpg alt="drawing" style="width:500px"> </center>

# <center> Проект: Задача регрессии. Предсказание общей продолжительности поездки на такси в Нью-Йорке. </center>

## Оглавление
1. [Задача проекта](#задача-проекта)
2. [Описание проекта](#описание-проекта)
3. [Описание данных](#описание-данных)
4. [Используемые версии](#используемые-версии)
5. [Установка проекта](#установка-проекта)
6. [Использование проекта](#использование-проекта)
7. [Авторы](#авторы)
8. [Выводы](#выводы)

## Задача проекта

### _Бизнес задача:_
Определить характеристики и с их помощью спрогнозировать длительность поездки на такси.

### _Техническая задача как для специалиста в Data Science:_
Построить модель машинного обучения, которая на основе предложенных характеристик клиента будет предсказывать числовой признак — время поездки такси, то есть решить задачу регрессии.

:arrow_up:[к оглавлению](#оглавление)

## Описание проекта
Необходимо проанализировать данные предоставленные в ходе проведения [соревнования на Kaggle](https://www.kaggle.com/competitions/nyc-taxi-trip-duration/overview). Выявить закономерность и найти решающие факторы, которые помогут спрогнозировать время поездки такси.


**Основные этапы работы над проектом:**
* Постановка задачи
* Знакомство с данными, базовый анализ и расширение данных
* Разведывательный анализ данных (EDA)
* Отбор и преобразование признаков
* Решение задачи регрессии: линейная регрессия и деревья решений
* Решение задачи регрессии: ансамблевые методы и построение прогноза
* Вывод

**Что практикуем при выполнении проекта**

Пактикуем и используем все полученные знания на практике. Самостоятельно используем все инструменты для работы с данными и построения модели.

**О структуре проекта**
* data - папка с исходными табличными данными.
* .gitignore - файл который исключает папку /data из репозитория 
* [Project_5.ipynb](./Project_5.ipynb) - jupiter-ноутбук, содержащий основной код проекта

:arrow_up:[к оглавлению](#оглавление)

## Описание данных
В этом проекте используются [train.csv](https://drive.google.com/file/d/1X_EJEfERiXki0SKtbnCL9JDv49Go14lF/view), [osrm_data_train.csv](https://drive.google.com/file/d/1ecWjor7Tn3HP7LEAm5a0B_wrIfdcVGwR/view),
[weather_data.csv](https://lms-cdn.skillfactory.ru/assets/courseware/v1/0f6abf84673975634c33b0689851e8cc/asset-v1:SkillFactory+DSPR-2.0+14JULY2021+type@asset+block/weather_data.zip),
[holiday_data.csv](https://lms-cdn.skillfactory.ru/assets/courseware/v1/33bd8d5f6f2ba8d00e2ce66ed0a9f510/asset-v1:SkillFactory+DSPR-2.0+14JULY2021+type@asset+block/holiday_data.csv),
[Project5_test_data.csv](https://drive.google.com/file/d/1C2N2mfONpCVrH95xHJjMcueXvvh_-XYN/view?usp=sharing),
[Project5_osrm_data_test.csv](https://drive.google.com/file/d/1wCoS-yOaKFhd1h7gZ84KL9UwpSvtDoIA/view?usp=sharing)

:arrow_up:[к оглавлению](#оглавление)

## Используемые версии
* Python (3.11.9):
    * [pandas (2.0.1)](https://pandas.pydata.org/docs/whatsnew/v2.0.1.html)
    * [numpy (1.24.2)](https://numpy.org/devdocs/release/1.24.2-notes.html)
    * [matplotlib (3.10.8)](https://matplotlib.org/3.10.8/index.html)
    * [seaborn (0.13.2)](https://seaborn.pydata.org/)
    * [scikit-learn (1.9.1)](https://scikit-learn.org/stable/)
    * [xgboost (3.2.0)](https://xgboost.readthedocs.io/en/release_3.2.0/)

:arrow_up:[к оглавлению](#оглавление)

## Установка проекта

```
git clone https://github.com/ret4ed/SF_Project_5.git
```

:arrow_up:[к оглавлению](#оглавление)

## Использование проекта
Вся информация о работе представлена в jupiter-ноутбуке [Project_5.ipynb](./Project_5.ipynb)

:arrow_up:[к оглавлению](#оглавление)

## Авторы
ret4ed (https://github.com/ret4ed)

:arrow_up:[к оглавлению](#оглавление)

## Выводы
В результате проделанной работы, были разобраны и обработы данные. Проведен разведывательный анализ с последующим отбором и преобразованием признаков. Задача была решена различными способами, при помощи: Линейной регрессии, Полиномиальной регрессии второй степени,  полиномиальной регрессиивторой степени с L2-регуляризацией, Деревьев решений, Случайного леса, Градиентного бустинга и XGBoost. Финалом данной работы является отправка submission-файла на платформу Kaggle.

:arrow_up:[к оглавлению](#оглавление)