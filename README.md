# Airbus CMS

## Installation
0. Install python3 or make virutalenv
1. Install the dependencies using `pip`
```bash
$ pip install -r requirements.txt
```
2. migrate the db
```bash
./manage.py migrate
```
3. make superuser to access admin
```bash
./manage.py createsuperuser
```
