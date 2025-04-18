# FoxPost

Добро пожаловать в проект **FoxPost**, созданный на основе фреймворка **Django**. Этот проект позволяет пользователям просматривать последние новости, добавлять комментарии и взаимодействовать с контентом. Чтобы сделать платформу более информативной, мы добавили функционал для автоматического парсинга новостей с других порталов. Это позволяет пользователям быть в курсе последних событий, собранных с различных веб-ресурсов, что значительно расширяет охват информации.

## Описание

Данный новостной портал предоставляет платформу для просмотра и обсуждения новостей. Он включает в себя следующие функции:

- Аутентификация пользователей (регистрация, вход, выход).
- Возможность комментирования новостей.
- Фильтрация и поиск новостей по категориям и ключевым словам.

## Установка

Следуйте этим шагам для установки проекта:

1. **Клонируйте репозиторий**:
   
```git clone https://github.com/AlenaAndrievska/foxpost.git```
```cd novosti-portal```

3. **Создайте виртуальное окружение и активируйте его**:
   
    ```python -m venv venv```
    ```source venv/bin/activate```
   
5. **Настройте базу данных**:
   
Убедитесь, что у вас установлен PostgreSQL или SQLite. Настройте конфигурацию базы данных в settings.py, а затем выполните миграции:

```python manage.py migrate```

4. **Создайте суперпользователя (для доступа к админке)**:

   ```python manage.py createsuperuser```

5. **Запустите сервер разработки**:

    ```python manage.py runserver```
   
Теперь вы можете открыть браузер и перейти по адресу http://127.0.0.1:8000 для доступа к новостному порталу.

## Использование
После успешной установки и запуска сервера вы можете:
- Зарегистрироваться или войти в систему как пользователь.
- Просматривать последние новости.
- Комментировать новости и взаимодействовать с другими пользователями.
- 
## Технологии

В этом проекте используются следующие технологии:
- Python 3.x
- Django 3.x
- PostgreSQL или SQLite (в зависимости от ваших предпочтений)
- HTML, CSS, JavaScript для фронтенда
- Beautiful Soup для автоматического получения новостей с других порталов
  
## Сотрудничество

Если вы хотите внести свой вклад в проект, пожалуйста, создайте ответвление (fork) репозитория, внесите необходимые изменения и создайте Pull Request. Мы будем рады вашим предложениям и замечаниям!
