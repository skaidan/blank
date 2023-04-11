FROM python:3.11-alpine

EXPOSE 8000

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
#RUN apt-get update && apt-get install -y libpq-dev gcc python3-dev musl-dev

ADD ./project /code
WORKDIR /code

RUN pip install --upgrade pip

RUN pip install \
    djangorestframework \
    django-rest-swagger \
    django-extensions \
    markdown \
    psycopg2-binary \
    django-filter \ 
    faker \ 
    factory-boy

CMD  python3 init.py && python manage.py runserver 0.0.0.0:8000
#CMD python entrypoint.py
