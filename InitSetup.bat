conda create --name MyDjangoEnv python=3.7

conda activate MyDjangoEnv
cd MyDjangoProject

pip install django
pip install faker
pip install pylint-django
pip install bcrypt
pip install django[argon2]
pip install pillow
pip install django-tastypie

set DJANGO_SETTINGS_MODULE=MyDjangoProject.settings

python fakePopulate.py
python manage.py migrate
python manage.py makemigrations MainApp
python manage.py makemigrations FormApp 
python manage.py makemigrations AuthApp 
python manage.py migrate


python manage.py createsuperuser

