## Проект YaMDb (final)

![workflow](https://github.com/Vlad540700/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

Проект  **YaMDb** собирает **отзывы (Review)** пользователей на **произведения (Titles)**. Произведения делятся на категории: "Книги", "Фильмы", "Музыка". Список **категорий (Category)** может быть расширен администратором.

Сами произведения в **YaMDb** не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

IP боевого сервера: 51.250.8.198

Работоспособность страниц можно проверить по следующим адресам:

1) http://51.250.8.198/api/v1/
2) http://51.250.8.198/admin
3) http://51.250.8.198/redoc

В каждой категории есть **произведения**: книги, фильмы или музыка. Например, в категории "Книги" могут быть произведения "Винни Пух и все-все-все" и "Марсианские хроники", а в категории "Музыка" — песня "Давеча" группы "Насекомые" и вторая сюита Баха.

Произведению может быть присвоен **жанр** (**Genre**) из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). Новые жанры может создавать только администратор.

Благодарные или возмущённые пользователи оставляют к произведениям текстовые **отзывы** (**Review**) и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — **рейтинг** (целое число). На одно произведение пользователь может оставить только один отзыв.


## Технологии

- Python 3.7

- Django 2.2.19

- Nginx

- Docker-compose


## Ресурсы API YaMDb

- Ресурс **auth**: аутентификация.

- Ресурс **users**: пользователи.

- Ресурс **titles**: произведения, к которым пишут отзывы (определённый фильм, книга или песенка).

- Ресурс **categories**: категории (типы) произведений («Фильмы», «Книги», «Музыка»).

- Ресурс **genres**: жанры произведений. Одно произведение может быть привязано к нескольким жанрам.

- Ресурс **reviews**: отзывы на произведения. Отзыв привязан к определённому произведению.

- Ресурс **comments**: комментарии к отзывам. Комментарий привязан к определённому отзыву.



## Пользовательские роли

- **Аноним** — может просматривать описания произведений, читать отзывы и комментарии.

- **Аутентифицированный пользователь (user)** — может читать всё, как и 

- **Аноним**, может публиковать отзывы и ставить оценки произведениям (фильмам/книгам/песенкам), может комментировать отзывы; может редактировать и удалять свои отзывы и комментарии, редактировать свои оценки произведений. Эта роль присваивается по умолчанию каждому новому пользователю.

- **Модератор (moderator)** — те же права, что и у **Аутентифицированного пользователя**, плюс право удалять и редактировать **любые** отзывы и комментарии.

- **Администратор (admin)** — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.

- **Суперюзер Django** должен всегда обладать правами администратора, пользователя с правами admin. Даже если изменить пользовательскую роль суперюзера — это не лишит его прав администратора. Суперюзер — всегда администратор, но администратор — не обязательно суперюзер.


## Шаблон наполнения env-файла:

1. Указываем, секретный ключ для settings.py:
```
SECRET_KEY=default-key
```
2. Указываем, что работаем с postgresql:
```
DB_ENGINE=django.db.backends.postgresql
```
3. Указываем имя базы данных:
```
DB_NAME=postgres
```
4. Указываем логин для подключения к базе данных:
```
POSTGRES_USER=login
```
5. Указываем пароль для подключения к БД:
```
POSTGRES_PASSWORD=password
```
6. Указываем название сервиса (контейнера):
```
DB_HOST=db
```
7. Указываем порт для подключения к БД:
```
DB_PORT=5432
```

## Установка

Для запуска приложения проделайте следующие шаги:

1. Склонируйте репозиторий.
2. Перейдити в папку infra и запустите docker-compose.yaml (при установленном и запущенном Docker)
```
docker-compose up
```
3. Для пересборки контейнеров выполните команду:
```
docker-compose up -d --build
```
4. В контейнере web выполните миграции:
```
docker-compose exec web python manage.py migrate
```
5. Создатйте суперпользователя:
```
docker-compose exec web python manage.py createsuperuser
```
6. Соберите статику:
```
docker-compose exec web python manage.py collectstatic --no-input
```
Проект запущен и доступен по адресу: [localhost](http://localhost/admin/)

## Загрузка тестовых значений в БД

Чтобы загрузить тестовые значения в базу данных перейдите в каталог проекта и скопируйте файл базы данных в контейнер приложения:
```
docker cp <DATA BASE> <CONTAINER ID>:/app/<DATA BASE>
```
Перейдите в контейнер приложения и загрузить данные в БД: 
```
docker container exec -it <CONTAINER ID> bash
python manage.py loaddata <DATA BASE>
```