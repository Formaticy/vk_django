# vk_django
Проект на Django. Social Network.
Описание: с помощью данного приложения можно создавать пользователей и настраивать между ними 
дружеские связи (отправлять заявки, принимать/отклонять их и т.п.).

## Структура проекта:
  - DjangoAPI. Там прописаны базовые конфигурации, например подключение к БД (использован .env)
  - SocialNetworkApp. Само приложение
    - models.py ==> Модели Users, Friends, Statuses реализованы для ORM (прописаны названия полей, связи)
    - serializers.py ==> Классы, реализующие сериализатор (из объектов в json и наоборот)
    - views.py ==> Классы, выполняющие функцию контроллера (обрабатывают входящий запрос)
    - urls.py ==> url паттерны для каждого класса-контроллера из views.py

# Запуск приложения
1. В консоли прописываем python manage.py runserver
2. Приложение доступно по адресу "http://127.0.0.1:8000/swagger/" в формате openAPI swagger

# Скриншоты работы
Общий вид при запуске
<image src="screenshots/общий вид при запуске в swagger.jpg" alt="Текст с описанием картинки">
  
# методы для модели friends:
  - GET /friends/ => получение информации о всех связях всех пользователей
  - POST /friends/ => отправка заявки в друзья
  - PUT /friends/delete/ => удаление из друзей
  - PUT /friends/detail/accept_proposal/ => принять заявку
  - GET /friends/detail/already_friends/{friend_one_id}/ => список друзей для юзера с id=friend_one_id
  - GET /friends/detail/incoming_proposals/{friend_one_id}/ => входящие заявки в друзья для юзера с id=friend_one_id
  - GET /friends/detail/outcoming_proposals/{friend_one_id}/ => исходящие заявки в друзья для юзера с id=friend_one_id
  - PUT /friends/detail/reject_proposal/ => отклонить заявку в друзья
  - GET /friends/detail/status/{friend_one_id}/{friend_two_id}/ => узнать статус отношений
<image src="screenshots/методы для модели friends.jpg" alt="Текст с описанием картинки">
  
  # методы для модели statuses:
  - GET /statuses/ => получение информации о всех статусах
  - POST /statuses/ => ввести новый статус
  - GET /statuses/{statusesId}/ => получение инф-ии о статусе по его id
  - PUT, PATCH /statuses/{statusesId}/ => изменение инф-ии о статусе по его id
  - DELETE /statuses/{statusesId}/ => удаление статуса 
<image src="screenshots/методы для модели statuses.jpg" alt="Текст с описанием картинки">
  
  # методы для модели users:
  - GET /users/ => получение информации о всех пользователях
  - POST /users/ => регистрация нового пользователя, (только с уникальным именем)
  - GET /users/{username}/ => получение инф-ии о юзере по его имени
  - PUT /users/{username}/ => изменение инф-ии о юзере по его имени
  - DELETE /users/{statusesId}/ => удаление юзера 
<image src="screenshots/методы для модели users.jpg" alt="Текст с описанием картинки">
  
  # Скриншоты по выполнению заданий
  # - Зарегистрировать нового пользователя
      1. получение всех пользователей
  <image src="screenshots/получение всех пользователей.jpg" alt="Текст с описанием картинки">
      2. POST запрос на добавление нового пользователя с примером запроса
<image src="screenshots/POST запрос на добавление нового пользователя с примером запроса.jpg" alt="Текст с описанием картинки">
      3. попытка добавить c неуникальным именем
<image src="screenshots/попытка добавить неуникальным именем.jpg" alt="Текст с описанием картинки">
      4. ошибка на добавление дубликата
  <image src="screenshots/ошибка на добавление дубликата.jpg" alt="Текст с описанием картинки">
      5. уникальный пользователь добавлен
      <image src="screenshots/уникальный пользователь добавлен.jpg" alt="Текст с описанием картинки">
      6. получение всего списка из таблицы users (c новым пользователем)
              <image src="screenshots/список пользователей вместе с новым.jpg" alt="Текст с описанием картинки">







