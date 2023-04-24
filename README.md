# newspaper

Новостной сайт на Django в Docker-контейнере

## Стек

<img src="https://img.shields.io/badge/Python-8F8FA6?style=for-the-badge&logo=Python&logoColor=3776AB"/>    
<img src="https://img.shields.io/badge/django-8F8FA6?style=for-the-badge&logo=Django&logoColor=092E20"/>     
<img src="https://img.shields.io/badge/PostgreSQL-8F8FA6?style=for-the-badge&logo=PostgreSQL&logoColor=4169E1"/>      
<img src="https://img.shields.io/badge/Docker-8F8FA6?style=for-the-badge&logo=Docker&logoColor=2496ED"/>


## Запуск приложения

### Клонирование репозитория:
````
git clone https://github.com/Ruslan-Gabbazov/newspaper.git
cd ./newspaper
````
### Создание и запуск Docker-контейнера:
````
docker-compose up
````
### Применение миграций:
В новой вкладке терминала:
````
docker-compose exec web python manage.py migrate
````
## Cайт:
Перейти в браузере на страницу: ```http://127.0.0.1:8000/news```
