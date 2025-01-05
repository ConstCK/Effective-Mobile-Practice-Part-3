# Приложение "Выставка собак" на DRF.

* Скопируйте проект к себе на ПК при помощи: git clone https://github.com/ConstCK/Effective-Mobile-Practice-Part-3.git
* Перейдите в папку проекта
* В терминале создайте виртуальное окружение (например python -m venv venv) и активируйте его (venv\scripts\activate)
* Установите все зависимости при помощи pip install -r requirements.txt
* Создайте файл .env в каталоге проекта и пропишите в нем настройки по примеру .env.example
* Например ключ для Django можно сгенерировать в python консоли при помощи
"from django.core.management.utils import get_random_secret_key", "get_random_secret_key()"
* Запустите сервер из каталога проекта (python manage.py runserver)

## EndPoints:
* localhost:8000/api/dogs/ - GET - Получение списка всех собак
* localhost:8000/api/dogs/id/ - GET - Получение собаки с указанным id
* localhost:8000/api/dogs/ - POST - Добавление собаки по шаблону
* localhost:8000/api/dogs/id/ - PUT - Изменение данных о собаке с указанным id по шаблону
* localhost:8000/api/dogs/id/ - DELETE - Удаление данных о собаке с указанным id
* localhost:8000/api/breeds/ - GET - Получение списка всех пород собак
* localhost:8000/api/breeds/id/ - GET - Получение породы с указанным id
* localhost:8000/api/breeds/ - POST - Добавление породы по шаблону
* localhost:8000/api/breeds/id/ - PUT - Изменение данных о породе с указанным id по шаблону
* localhost:8000/api/breeds/id/ - DELETE - Удаление данных о породе с указанным id

## Шаблоны:
### Для создания/изменения собак

{
    "name": "Dog's name",
    "age": 3,
    "gender": "FEMALE/MALE",
    "color": "Dog's color",
    "favourite_food": "Some Food",
    "favourite_toy": "Some toy",
    "breed": 2
}

### Для создания/изменения породы собак

{
    "name": "Breed",
    "size": "TINY/SMALL/MEDIUM/LARGE",
    "friendliness": 1,
    "trainability": 5,
    "shedding_amount": 1,
    "exercise_needs": 3
}

## Для запуска приложение в контейнере:
* **Docker Desktop должен быть запущен
* Команда запуска из директории проекта из консоли docker-compose up**

Endpoints:
ВСЕ ВЫШЕПЕРЕЧИСЛЕННЫЕ +
* localhost:8080/ - Администрирование БД в контейнере
