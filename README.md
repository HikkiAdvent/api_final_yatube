

---

### Описание

Проект предоставляет REST API для взаимодействия с социальной сетью, где пользователи могут создавать и просматривать посты, оставлять комментарии, а также подписываться на других пользователей.

Основной функционал включает:
- **Создание постов**: пользователи могут публиковать текстовые записи с возможностью добавления изображений и выбора группы.
- **Комментарии**: пользователи могут оставлять комментарии под постами.
- **Подписки**: пользователи могут подписываться на других пользователей, чтобы следить за их активностью.
- **Группы**: пользователи могут присоединяться к тематическим группам, что позволяет организовать контент по интересам.
- **Пагинация**: поддержка выдачи результатов с ограничением и смещением через параметры `limit` и `offset`.

### Установка

1. Клонировать репозиторий и перейти в него в командной строке:

    ```bash
    git clone https://github.com/HikkiAdvent/api_final_yatube.git
    ```

    ```bash
    cd api_final_yatube
    ```

2. Создать и активировать виртуальное окружение:

    ```bash
    python3 -m venv env
    ```

    ```bash
    source env/bin/activate
    ```

3. Установить зависимости из файла `requirements.txt`:

    ```bash
    python3 -m pip install --upgrade pip
    ```

    ```bash
    pip install -r requirements.txt
    ```

4. Выполнить миграции для создания необходимых таблиц в базе данных:

    ```bash
    python3 manage.py migrate
    ```

5. Запустить проект:

    ```bash
    python3 manage.py runserver
    ```

### Основные эндпоинты API

- **/posts/** (GET, POST)
  - Получение списка постов, создание нового поста.
  - Поддержка параметров пагинации: `limit` и `offset`.

- **/posts/{id}** (GET, PUT, PATCH, DELETE)
  - Получение поста, изменение и удаление.

- **/posts/{id}/comments/** (GET, POST)
  - Получение комментариев к посту, добавление нового комментария.

- **/posts/{id}/comments/{comment_id}** (GET, PUT, PATCH, DELETE)
  - Получение комментария, изменение и удаление.

- **/groups/** (GET)
  - Получение списка доступных групп.

- **/groups/{id}** (GET)
  - Получение отдельной группы.

- **/follow/** (GET, POST)
  - Получение списка подписок текущего пользователя, создание подписки на другого пользователя.
  - С параметром *search* можно выполнять поиск по частичным совпадениям.
### Примеры запросов и ответов

1. **Получить список всех публикаций**:

    Пример запроса:
    ```
    GET /posts/?limit=10&offset=0
    ```

    Пример ответа:
    ```json
    {
      "count": 123,
      "next": "http://api.example.org/posts/?offset=10&limit=10",
      "previous": null,
      "results": [
        {
          "id": 1,
          "author": "user1",
          "text": "Моя первая запись",
          "pub_date": "2023-05-01T12:00:00Z",
          "image": "http://example.com/media/posts/image.jpg",
          "group": 2
        }
        ...
      ]
    }
    ```

2. **Создать новый пост**:

    Пример запроса:
    ```
    POST /posts/
    ```

    Пример тела запроса:
    ```json
    {
      "text": "Это мой новый пост",
      "group": 1,
      "image": null
    }
    ```

    Пример ответа:
    ```json
    {
      "id": 10,
      "author": "user1",
      "text": "Это мой новый пост",
      "pub_date": "2023-05-01T12:05:00Z",
      "image": null,
      "group": 1
    }
    ```

3. **Оставить комментарий к посту**:

    Пример запроса:
    ```
    POST /posts/{post_id}/comments/
    ```

    Пример тела запроса:
    ```json
    {
      "text": "Отличный пост!"
    }
    ```

    Пример ответа:
    ```json
    {
      "id": 1,
      "author": "user2",
      "text": "Отличный пост!",
      "created": "2023-05-01T12:10:00Z",
      "post": 10
    }
    ```

4. **Подписаться на пользователя**:

    Пример запроса:
    ```
    POST /follow/
    ```

    Пример тела запроса:
    ```json
    {
      "following": "user2"
    }
    ```

    Пример ответа:
    ```json
    {
      "user": "user1",
      "following": "user2"
    }
    ```

### Технологии

- **Django** и **Django REST Framework** для реализации API.
- **SQLite** в качестве базы данных.
- **JWT** для аутентификации пользователей.

### Автор

 *Валерий Петренко*

---
