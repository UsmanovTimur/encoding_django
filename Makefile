build:
	docker build -t encoding_django .

runserver:
	docker run -p 8000:8000 -it encoding_django
