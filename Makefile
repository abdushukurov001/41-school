.SILENT:
.ONSHELL:
.PHONY:default

default:
	echo "commands are: clean, build, run, stop, refresh"

clean:
	docker rm school-4-container
	docker rmi school-4:latest

build:
	docker build -t school-4 .

run:
	docker run -d --name school-4-container --restart unless-stopped -p 8001:8000 -v .:/opt/project school-4

stop:
	docker stop school-4-container

migrate:
	python3 ./manage.py migrate

collect-static:
	python3 ./manage.py collectstatic --no-input

run-server:migrate collect-static
	python3 ./manage.py runserver 0.0.0.0:8000

refresh: stop clean build run