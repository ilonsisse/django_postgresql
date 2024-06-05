# Примечание
**README.md и .gitignore удалить перед видео!!**
# Алгоритм
1. Качаем Python: https://www.python.org/downloads/
2. При установке добавляем галочку в PATH
3. Если команда pip в терминале все равно не работает, то загружаем отсюда: https://disk.yandex.ru/d/E4wGXGnRhlw3Hw . Далее заходим в терминал и пишем 
   > py(в macOS python3) путь_к_файлу. Пример: py C:\get-pip-2.py
4. Скачиваем СУБД PostgreSQL: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
5. В установщике ничего не меняем, придуманный пароль запоминаем
6. Заходим в папку с установленным PostgreSQL, в папку bin и копируем полный путь до **psql**
7. Открываем Свойства компьютера -> дополнительные настройки -> переменные окружения -> изменить -> добавить -> вставляем путь до psql
8. Открываем консоль, пишем
   > chcp 1252

   > psql -U postgres
9.  Создаем базу данных:
    > CREATE DATABASE django_agamirov;

    > CREATE USER admin WITH PASSWORD 'very_strong_password';

    > ALTER ROLE admin SET client_encoding TO 'utf8';

    > ALTER ROLE admin SET default_transaction_isolation TO 'read committed';

    > ALTER ROLE admin SET timezone TO 'UTC';

    > GRANT ALL PRIVILEGES ON DATABASE django_agamirov TO admin;

    > GRANT postgres TO admin;

    > exit
10. Открываем проект в PyCharm
11. Открываем консоль в PyCharm, пишем
   > py -m venv djvenv
12. Запускаем виртуальное окружение
   > Windows: .\djvenv\Scripts\activate

   > macOS и Linux: source djvenv/bin/activate
13. Далее вводим и перегазгружаем PyCharm
   > pip install -r requirements.txt
14. Помечаем корневую папку со всеми файлами как sources root в PyCharm: ПКМ на корневую папку -> в самом низу Mark directory as -> Sources root
15. Пишем в консоли и создаем суперпользователя
    > py manage.py createsuperuser
16. Скачиваем OBS: https://obsproject.com/ru
17. Во втором разделе Sources добавляем **Screen Capture** и **Audio Input Capture**
18. Если хотим записать весь экран, а не программу, то нужно убедиться, что OBS захватывает весь экран. Заходим в настройки -> video -> Base и Output Resoluiton должны быть в одном разрешении
19. В третьем разделе нажимаем **Start Recording**
20. Там же потом нажимаем на **Stop Recording**
21. После записи внизу OBS покажет, куда он сохранил видео 
# Что говорить на видео
**Примечание**: не открывать сайт проекта, он не работает нормально
- Я установил Django и необходимые библиотеки. Показываем файл в корневой папке **requirements.txt**
- 