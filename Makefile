.SILENT:
.ONSHELL:
.PHONY:default

default:
	echo "commands are: clean, build, run, stop, refresh"

clean:
	docker rmi school-4:latest

build:
	docker build -t school-4 .

run:
	docker run -d --name school-4-container -p 8001:8000 -v .:/opt/project school-4

stop:
	docker stop school-4-container

refresh: stop clean build run