FROM python:2.7

RUN mkdir /srv/app
WORKDIR /srv/app

COPY . .
RUN pip install -r requirements.txt

CMD python manage.py runserver
