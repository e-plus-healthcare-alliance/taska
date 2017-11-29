build:
	docker build -t bioinformatics-ua/workflow-management:latest .

run:
	sh bin/clean_container.sh && \
	docker-compose up --no-recreate -d

stop:
	docker-compose stop

clean:
	docker-compose rm -f

