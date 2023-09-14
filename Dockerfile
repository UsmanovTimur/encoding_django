FROM python:3.11
ENV PYTHONUNBUFFERED 1
ENV LANG=C.UTF-8
RUN mkdir /code
COPY . /code/
WORKDIR /code
RUN rm -r venv/
RUN pip install -r requirements.txt
RUN python encrypt.py .
RUN nuitka3 --module --nofollow-imports --static-libpython=no --remove-output --no-pyi-file --jobs=4 loader.py && rm loader.py
CMD python manage.py runserver 0.0.0.0:8000
