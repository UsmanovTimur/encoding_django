FROM python:3.11
ENV PYTHONUNBUFFERED 1
ENV LANG=C.UTF-8
RUN mkdir /code
COPY . /code/
WORKDIR /code
RUN rm -r venv/
RUN pip install -r requirements.txt
RUN python encrypt.py .
CMD python manage.py runserver 0.0.0.0:8000
