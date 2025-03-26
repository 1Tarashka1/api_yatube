# API для проекта Yatube
Yatube — это платформа социальных сетей, которая позволяет пользователям создавать учетные записи, размещать свои посты, подписываться на интересующих авторов и оставлять комментарии к их публикациям.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

shell

git clone https://github.com/1Tarashka1/api_yatube.git

Cоздать и активировать виртуальное окружение:

shell

python -m venv venv

shell

source venv/Scripts/activate

Установить зависимости из файла requirements.txt:

shell

python -m pip install --upgrade pip

shell

pip install -r requirements.txt

Выполнить миграции из директории yatube_api:

shell

python manage.py migrate

Запустить проект:

shell

python manage.py runserver

### Получить токен для авторизации:

Создать суперпользователя

shell

python manage.py createsuperuser

или обычного пользователя через админку ../admin (войти через созданного суперпользователя)

Отправить на эндпоинт ../api/v1/jwt/create/ имя и пароль созданного пользователя/суперпользователя в теле запроса. Ожидаемый ответ:

JSON

{
  "refresh": "string",
  "access": "string"
}

Токен access передавать в заголовке каждого запроса, в поле Authorization, иначе вернётся *HTTP 401 Unauthorized*. Перед самим токеном должно стоять ключевое слово Bearer и пробел.

### Примеры запросов

Пример POST-запроса с токеном Антона Чехова: добавление нового поста.
POST .../api/v1/posts/

{
    "text": "Вечером собрались в редакции «Русской мысли», чтобы поговорить о народном театре. Проект Шехтеля всем нравится."
} 

Пример ответа:

{
    "id": 14,
    "text": "Вечером собрались в редакции «Русской мысли», чтобы поговорить о народном театре. Проект Шехтеля всем нравится.",
    "author": "anton",
    "image": null,
    "group": 1,
    "pub_date": "2021-06-01T08:47:11.084589Z"
} 

Пример POST-запроса с токеном Антона Чехова: отправляем новый комментарий к посту с id=14.
POST .../api/v1/posts/14/comments/

{
    "text": "тест тест",
} 

Пример ответа:

{
    "id": 4,
    "author": "anton",
    "post": 14,
    "text": "тест тест",
    "created": "2021-06-01T10:14:51.388932Z"
} 

Пример GET-запроса с токеном Антона Чехова: получаем информацию о группе.
GET .../api/v1/groups/2/

Пример ответа:

{
    "id": 2,
    "title": "Математика",
    "slug": "math",
    "description": "Посты на тему математики"
} 
