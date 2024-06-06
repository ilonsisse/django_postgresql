# Примечание
**README.md и .gitignore удалить перед видео!!**
# Алгоритм
1. Качаем Python: https://www.python.org/downloads/
2. При установке добавляем галочку в PATH
3. Если команда pip в терминале все равно не работает, то загружаем отсюда: https://disk.yandex.ru/d/E4wGXGnRhlw3Hw . Далее заходим в терминал и пишем 
   > py(в macOS python3) путь_к_файлу. Пример: py C:\get-pip-2.py
4. Скачиваем: 
   > VS Code: https://code.visualstudio.com/ + REST Client: https://marketplace.visualstudio.com/items?itemName=humao.rest-client
5. Скачиваем СУБД PostgreSQL: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
6. В установщике ничего не меняем, придуманный пароль запоминаем
7. Заходим в папку с установленным PostgreSQL, в папку bin и копируем полный путь до **psql**
8. Открываем Свойства компьютера -> дополнительные настройки -> переменные окружения -> изменить -> добавить -> вставляем путь до psql
9.  Открываем консоль, пишем
   > chcp 1252

   > psql -U postgres
10. Создаем базу данных:
    > CREATE DATABASE django_agamirov;

    > CREATE USER admin WITH PASSWORD 'very_strong_password';

    > ALTER ROLE admin SET client_encoding TO 'utf8';

    > ALTER ROLE admin SET default_transaction_isolation TO 'read committed';

    > ALTER ROLE admin SET timezone TO 'UTC';

    > GRANT ALL PRIVILEGES ON DATABASE django_agamirov TO admin;

    > GRANT postgres TO admin;

    > exit
11. Открываем проект в PyCharm
12. Открываем консоль в PyCharm, пишем
   > py -m venv djvenv
13. Запускаем виртуальное окружение
   > Windows: .\djvenv\Scripts\activate

   > macOS и Linux: source djvenv/bin/activate
14. Далее вводим
   > pip install -r requirements.txt
15. Помечаем корневую папку со всеми файлами как sources root в PyCharm: ПКМ на корневую папку -> в самом низу Mark directory as -> Sources root
16. Запускаем сервер
    > py manage.py runserver
17. Открываем файл **requests.http** в VS Code и проверяем, работает ли API, нажимая на **Send request**
18. Скачиваем OBS: https://obsproject.com/ru
19. Во втором разделе Sources добавляем **Screen Capture** и **Audio Input Capture**
20. Если хотим записать весь экран, а не программу, то нужно убедиться, что OBS захватывает весь экран. Заходим в настройки -> video -> Base и Output Resoluiton должны быть в одном разрешении
21. В третьем разделе нажимаем **Start Recording**
22. Там же потом нажимаем на **Stop Recording**
23. После записи внизу OBS покажет, куда он сохранил видео 
# Что говорить на видео
- Я установил Django и необходимые библиотеки. Показываем файл в корневой папке **requirements.txt**
- Установил СУБД PostgreSQL. Показываем настройки **DATABASES** в postgre_kr **settings.py**
- Создал модели Place и Shop и применил миграцию. Показываем файл в example **models.py**
- Создал сериализаторы для этих моделей. Показываем файл в example **serializers.py**
- Также реализовал ViewSet'ы для моделей Shop и Place. Показываем файл в example **views.py**
- Добавил эти ViewSet'ы в роутинг. Показываем файл в postgre_kr **urls.py**
- Теперь у проекта есть свой API. Покаываем файл в корне **requests.http** и тыкаем на случайные реквесты(Альтернативно можно просто зайти на сервер и сделать то же самое, только с графическим интерфейсом)
  