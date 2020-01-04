conda create --name MyDjangoEnv python=3.7

conda activate MyDjangoEnv
cd MyDjangoProject
pip install django
pip install faker
pip install pylint-django

python manage.py migrate
python manage.py makemigrations MyDjangoApp 
python manage.py migrate

set DJANGO_SETTINGS_MODULE=MyDjangoProject.settings

python manage.py createsuperuser
python manage.py runserver