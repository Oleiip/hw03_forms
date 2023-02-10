# hw03_forms - Сообщества создание записей

Добавлены следующие возможности:
- регистрация пользователя, 
- вход/выход пользователя,
- восстановления пароля,
- создания записей сообщества,
- подробная информация, редактирование только своей записи,
- отображение постов пользователя,
- пагинация, раздел Об авторе, Технологии, отображения профиля пользователя.

### Настройка и запуск на ПК

Клонируем проект:

```bash
git clone https://github.com/oleiip/hw03_forms.git
```

или

```bash
git clone git@github.com:oleiip/hw03_forms.git
```

Переходим в папку с проектом:

```bash
cd hw03_forms
```

Устанавливаем виртуальное окружение:

```bash
python -m venv venv
```

Активируем виртуальное окружение:

```bash
source venv/Scripts/activate
```

> Для деактивации виртуального окружения выполним (после работы):
> ```bash
> deactivate
> ```
Устанавливаем зависимости:

```bash
python -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

Применяем миграции:

```bash
python yatube/manage.py makemigrations
```
```bash
python yatube/manage.py migrate
```

Создаем супер пользователя:

```bash
python yatube/manage.py createsuperuser
```

В папку с проектом, где файл settings.py добавляем файл .env куда прописываем наши параметры:

```bash
SECRET_KEY='Ваш секретный ключ'
ALLOWED_HOSTS='127.0.0.1, localhost'
DEBUG=True
```

Не забываем добавить в .gitingore файлы:

```bash
.env
.venv
```

Для запуска тестов выполним:

```bash
pytest
```

Запускаем проект:

```bash
python yatube/manage.py runserver
```

Заходим в http://localhost/admin и создаем группы и записи.
После чего записи и группы появятся на главной странице.

