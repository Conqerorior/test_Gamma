<p align="center">
  <img src="https://hhcdn.ru/ichameleon/174243.png" alt="AlfaBankHackathon">
</p>

# Описание тестового проекта Гамма"
Проект **"test_Gamma"** представляет собой бэкенд-часть системы управления информацией о 
почтовых отправлениях. Система позволяет регистрировать два типа посылок: 
письма и посылки. Для каждого типа посылки предусмотрены различные характеристики.


# Технологии
<div id="header" align="center">
  <img src="https://img.shields.io/badge/Python-3.11.1-092E20?style=for-the-badge&logo=python&logoColor=20B2AA">
  
  <img src="https://img.shields.io/badge/Django-5.0.2-092E20?style=for-the-badge&logo=django&logoColor=20B2AA">
  
  <img src="https://img.shields.io/badge/Django%20REST%20framework-3.14.0-092E20?style=for-the-badge&logo=django&logoColor=20B2AA">

  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white">
  
  <img src="https://img.shields.io/badge/PostgreSQL-555555?style=for-the-badge&logo=postgresql&logoColor=20B2AA">
</div>

# Использование API
API доступно по адресу http://localhost:8000/api/.


* **Доступные эндпоинты**
  + **/api/letters/** - эндпоинт для работы с письмами.
  + **/api/packages/** - эндпоинт для работы с посылками.



#### Локальный запуск проекта

- Склонировать репозиторий:

```bash
   git clone <название репозитория>
```

```bash
   cd <название репозитория> 
```

- Cоздать и активировать виртуальное окружение:

- Команда для Windows:

```bash
   python -m venv venv
   source venv/Scripts/activate
```

- Установить зависимости из файла **requirements.txt**:

```bash
   cd ..
   cd backend
   pip install -r requirements.txt
```

```bash
   python manage.py migrate
```


- Создать суперпользователя:

```bash
python manage.py createsuperuser
```

- Запустить локальный сервер:

```bash
   python manage.py runserver
```


# Автор
**Сергей Овинцев**

**[Conqerorior](https://github.com/Conqerorior)**
