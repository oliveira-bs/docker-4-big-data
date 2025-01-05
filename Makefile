build : 
	@echo " ---- BUILD ---- "
	@docker-compose build

destroy :
	@echo " ---- DESTROY - DEFAULT ---- "
	@docker-compose down -v


start :
	@echo " ---- START ---- "
	@docker-compose up --build -d 
	@chmod +x ./containers/airflow/docker-entrypoint.sh
	@./containers/airflow/docker-entrypoint.sh

stop :
	@echo " ---- STOP ---- "
	@docker-compose down
