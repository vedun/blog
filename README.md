
Для запуска склонировать проект и запусть следующие команды в корневой директории:

* `python -m venv ve`
* `source ve/bin/activate`
* `pip install -r ./requirements_prod.txt`
* `pip install -r ./requirements_dev.txt`
* `./manage.py migrate`
* `./manage.py createsuperuser` - создание администратора
* `./manage.py runserver`

Страницы логина нет, входить через админку - `http://localhost:8000/admin`.
Само приложение находится в корне домена - `http://localhost:8000`.
