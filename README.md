
Для запуска склонировать проект и запусть следующие команды в корневой директории:

* `python -m venv ve`
* `source ve/bin/activate`
* `pip install -r ./requirements_prod.txt`
* `pip install -r ./requirements_dev.txt`
* `./manage.py migrate`
* `./manage.py runserver`

открыть страницу `http://localhost:8000` в браузере
