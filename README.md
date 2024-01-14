# Social Network app
Проект на Django. Social Network.
<h3>Описание</h3> C помощью данного приложения можно создавать пользователей и настраивать между ними 
дружеские связи (отправлять заявки, принимать/отклонять их и т.п.).

## Структура проекта:
  - DjangoAPI. Там прописаны базовые конфигурации, например подключение к БД (использован .env)
  - SocialNetworkApp. Само приложение
    - models.py ==> Модели Users, Friends, Statuses реализованы для ORM (прописаны названия полей, связи)
    - serializers.py ==> Классы, реализующие сериализатор (из объектов в json и наоборот)
    - views.py ==> Классы, выполняющие функцию контроллера (обрабатывают входящий запрос)
    - urls.py ==> url паттерны для каждого класса-контроллера из views.py

<h4 align="center">ОБЯЗАТЕЛЬНО ПЕРЕД ЗАПУСКОМ:</h4> 
Пояснение полей: <br>
  1. friend_one => id человека, которЫЙ ОТПРАВЛЯЕТ запрос в друзья <br>
  2. friend_two => id человека, которОМУ ОТПРАВЛЯЮТ запрос в друзья <br>
  
  - statusId => статус отношений между двумя пользователями (на фото пояснен каждый тип и их ID)
    <image src="screenshots/статусы.jpg" alt="Текст с описанием картинки">
  
 Пояснение общее: <br>
   1. В таблице Friends хранятся только отношения пользователей со статусами statusId = 2 (исходящая заявка) и statusId = 4 (уже друзья) <br>
  Всю информацию можно получить из этих двух статусов. Данное решение (сохранять только два статуса) принято для того, чтобы не сохранять в БД избыточную информацию и сэкономить место в памяти.

# Запуск приложения
1. В консоли прописываем python manage.py runserver
2. Приложение доступно по адресу "http://127.0.0.1:8000/swagger/" в формате openAPI swagger
 - Или использовать докер и запустить приложение командой `docker compose up`

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
                
# - Отправить одному пользователю заявку в друзья другому
      1. получение всего списка из таблицы friends
<image src="screenshots/получение всего списка из таблицы friends.jpg" alt="Текст с описанием картинки">
      2. отправка заявки в друзья от id=8 к id=6
<image src="screenshots/отправка заявки в друзья от id=8 к id=6.jpg" alt="Текст с описанием картинки">
      3. заявка успешно отправлена
<image src="screenshots/заявка успешно отправлена.jpg" alt="Текст с описанием картинки">
      4. еще одна отправка заявки в друзья от id=8 к id=3
<image src="screenshots/еще одна отправка заявки в друзья от id=8 к id=3.jpg" alt="Текст с описанием картинки">     
      5. еще одна отправка заявки в друзья от id=2 к id=8
<image src="screenshots/еще одна отправка заявки в друзья от id=2 к id=8.jpg" alt="Текст с описанием картинки">
      6. заявки (8, 3) (2, 8) успешно отправлены
<image src="screenshots/заявки (8, 3) (2, 8) успешно отправлены.jpg" alt="Текст с описанием картинки">
  
# - Принять/отклонить пользователю заявку в друзья от другого пользователя
  1. PUT запрос на отклонение заявок
<image src="screenshots/PUT запрос на отклонение заявок.jpg" alt="Текст с описанием картинки">
  2. отклонение заявки от id=2 к id=8 часть1
<image src="screenshots/отклонение заявки от id=2 к id=8 часть1.jpg" alt="Текст с описанием картинки">
  3. результат отклонения заявки от id=2 к id=8 часть 2
<image src="screenshots/результат отклонения заявки от id=2 к id=8 часть 2.jpg" alt="Текст с описанием картинки">
  4. результат отклонения заявки от id=2 к id=8 часть 3
<image src="screenshots/результат отклонения заявки от id=2 к id=8 часть 3.jpg" alt="Текст с описанием картинки">
  5. если отклонить несуществующую заявку
<image src="screenshots/если отклонить несуществующую заявку.jpg" alt="Текст с описанием картинки">
  6. принятие заявки от id=8 к id=3 часть1
<image src="screenshots/принятие заявки от id=8 к id=3 часть1.jpg" alt="Текст с описанием картинки">
  7. результат принятия заявки от id=8 к id=3 часть 2
<image src="screenshots/результат принятия заявки от id=8 к id=3 часть 2.jpg" alt="Текст с описанием картинки">
  8. результат принятия заявки от id=8 к id=3 часть 3
<image src="screenshots/результат принятия заявки от id=8 к id=3 часть 3.jpg" alt="Текст с описанием картинки">
  
# - Просмотреть пользователю список исходящих и входящих заявок в друзья
1. просмотр входящих заявок в друзья для id=8
<image src="screenshots/просмотр входящих заявок в друзья для id=8.jpg" alt="Текст с описанием картинки">
2. просмотр иходящих заявок в друзья для id=8
<image src="screenshots/просмотр иходящих заявок в друзья для id=8.jpg" alt="Текст с описанием картинки">
  
# - Просмотреть пользователю список своих друзей
1. список друзей для id=8
<image src="screenshots/список друзей для id=8.jpg" alt="Текст с описанием картинки">
2. список друзей для id=3
<image src="screenshots/список друзей для id=3.jpg" alt="Текст с описанием картинки">
3. список друзей для id=36 (несуществующего)
<image src="screenshots/список друзей для id=36 несуществующего.jpg" alt="Текст с описанием картинки">
 
# - Получить пользователю статус дружбы с каким-то другим пользователем
1. просмотр статуса осношений между id=8 и id=4
<image src="screenshots/просмотр статуса осношений между id=8 и id=4.jpg" alt="Текст с описанием картинки">
2. просмотр статуса осношений между id=8 и id=3
<image src="screenshots/просмотр статуса осношений между id=8 и id=3.jpg" alt="Текст с описанием картинки">
3. просмотр статуса осношений между id=3 и id=8
<image src="screenshots/просмотр статуса осношений между id=3 и id=8.jpg" alt="Текст с описанием"> 
4. просмотр статуса осношений между id=6и id=8
<image src="screenshots/просмотр статуса осношений между id=6и id=8.jpg" alt="Текст с описанием картинки">  
5. просмотр статуса осношений между id=8 и id=6
<image src="screenshots/просмотр статуса осношений между id=8 и id=6.jpg" alt="Текст с описанием картинки">  
  
  
  # - Удалить пользователю другого пользователя из своих друзей
1. удаление id=3 из друзей id=8 часть 1
<image src="screenshots/удаление id=3 из друзей id=8 часть 1.jpg" alt="Текст с описанием картинки">
2. удаление id=3 из друзей id=8 часть 2
<image src="screenshots/удаление id=3 из друзей id=8 часть 2.jpg" alt="Текст с описанием картинки">
3. удаление id=3 из друзей id=8 часть 3
<image src="screenshots/удаление id=3 из друзей id=8 часть 3.jpg" alt="Текст с описанием картинки">
4. удаление id=8 из друзей id=5 (не существует такой пары)
<image src="screenshots/удаление id=8 из друзей id=5 (не существует такой пары).jpg" alt="Текст с описанием картинки">
  
  # - Если пользователь1 отправляет заявку в друзья пользователю2, а пользователь2 отправляет заявку пользователю1, то они автоматом становятся друзьями, их заявки автоматом принимаются
1. отправка запроса в друзья от id=8 к id=5 для проверки последнего пункта
<image src="screenshots/отправка запроса в друзья от id=8 к id=5 для проверки последнего пункта.jpg" alt="Текст с описанием картинки">
2. для проверки последнего пункта часть 2
<image src="screenshots/для проверки последнего пункта часть 2.jpg" alt="Текст с описанием картинки">
3. для проверки последнего пункта часть 3 (успешно)
<image src="screenshots/для проверки последнего пункта часть 3 (успешно).jpg" alt="Текст с описанием картинки">
4. статус у данной пары обновлен на 4 = друзья (см. в самое начало)
<image src="screenshots/для проверки последнего пункта часть 4 статус изменен.jpg" alt="Текст с описанием картинки">
 <br>
 <br>
<h1> Планы на улучшение и доработку проекта:</h1>
  - Отправка заявок в друзья по имени, а не по Id  <br>
  - Передавть данные через query params string (https://test?param=key)   <br>
  - Написать фронтенд часть, GUI <br>
  - Добавить авторизацию и аутентификацию <br>
  
 
 






