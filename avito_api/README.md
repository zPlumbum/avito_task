# Инструкция по запуску
Для подготовки проекта к запуску необходимо подключить свою базу данных PostgreSQL в настройках 
Django (для этого вместо данных *your name* и т.д. введите свои). Затем примените миграции 
и загрузите фикстуры.
Запуск проекта производится командой *python manage.py runserver*

![Screenshot](images/db.png)
![Screenshot](images/runserver.png)

# Примеры запросов
### Создание пользователя:
![Screenshot](images/create1.png)
![Screenshot](images/create2.png)

### Получение данных о балансе:
![Screenshot](images/get1.png)
![Screenshot](images/get2.png)

### Пополнение и списание с баланса:
![Screenshot](images/replenishment1.png)
![Screenshot](images/replenishment2.png)

### Транзакция между пользователями:
![Screenshot](images/transaction1.png)
![Screenshot](images/transaction2.png)
