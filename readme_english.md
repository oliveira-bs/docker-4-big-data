# Docker for Big Data
See [Original readme](./readme.md)

## Project Objective
The "docker-4-big-data" project aims to create a Docker environment for efficiently orchestrating and processing Big Data in an **on-premise/development environment**. The use of **Docker containers** ensures portability and scalability, while leveraging tools such as **Apache Airflow** for workflow orchestration, **Apache Spark** for data processing, **PostgreSQL** for storage, and **LocalStack** for simulating AWS services, creates a robust environment for automating and handling large volumes of data. This setup is designed to run locally, enabling efficient data workflows with an emphasis on testing and development in a **data engineering** context.

## Tools Used
- **Apache Airflow** (version 2.10.4 with Python 3.12): Workflow orchestration.
- **Apache Spark** (image `bitnami/spark:3.5.4`): Distributed data processing.
- **PostgreSQL** (image `postgres:17.2`): Relational database replacing Airflow's default SQLite database, providing greater storage capacity and scalability for metadata. Also used for querying data.
- **LocalStack** (image `localstack/localstack:4.0.3`): Simulation of AWS services such as **S3**, **SNS**, **SQS**, **DynamoDB**, **Lambda**, and **API Gateway**, allowing for the emulation of a local AWS environment for testing and development.
- **Python**: Primary language used for scripts and dependencies, especially in Airflow.
- **Bash**: Used for the `docker-entrypoint.sh` initialization script and in the `Makefile`.

## Images and Versions Used
- **Apache Airflow**: `apache/airflow:2.10.4-python3.12`
- **Apache Spark**: `bitnami/spark:3.5.4`
- **LocalStack**: `localstack/localstack:4.0.3`
- **PostgreSQL**: `postgres:17.2`

## Docker Commands
Commands for managing the containers are defined in the `Makefile`, making Docker usage more straightforward. Users do not need to interact directly with Docker commands. The main commands are:

- **`make build`**: Builds the containers defined in `docker-compose.yml`.
  ```
  make build
  ```
- **`make destroy`**: Stops the containers and removes volumes.
  ```
  make destroy
  ```
- **`make start`**: Starts the containers, ensuring the Airflow Webserver is available.
  ```
  make start
  ```
- **`make stop`**: Stops the containers and removes associated resources.
  ```
  make stop
  ```

These commands automate processes and simplify project implementation and execution.

## Testing Communication Between Containers

In this section, we will verify the communication between the Airflow container and the **Spark** and **LocalStack** containers. To do this, we will run the scripts located in `src/`, which trigger the **Spark** container to process data and generate a new file in `data/output/processed/`, as well as create a new bucket in **LocalStack S3**.

- Testing data processing with Spark:

```
docker exec -it airflow /bin/bash -c "spark-submit --master spark://spark-master:7077 --packages org.apache.hadoop:hadoop-aws:3.3.1 /opt/airflow/src/app.py"
```

- Testing communication with LocalStack and creating a new bucket:

```
docker exec -it airflow /bin/bash -c "python3 /opt/airflow/src/make_bucket.py"
```

After execution, a new file should be available in `data/output/processed/`, and the new bucket should be visible in the **LocalStack** dashboard.

## Project Structure
The project follows the directory structure below:

```
docker-4-big-data/
├── containers/
|   ├── airflow/
|   │   ├── dags/
|   │   ├── logs/
|   │   ├── .env
|   │   ├── docker-entrypoint.sh
|   │   ├── Dockerfile
|   │   └── requirements.txt
|   ├── localstack/
|   │   ├── data/
|   │   |   ├── cache/
|   │   |   ├── lib/
|   │   |   ├── logs/
|   │   |   └── tmp/
|   │   └── .env
|   ├── postgres/
|   │   └── .env
|   ├── postgres-airflow/
|   │   └── .env
|   └── spark/
|       ├── configs/
|       |   ├── spark-master.env
|       |   └── spark-worker.env
|       └── .env
├── data/
│   ├── landing/
│   ├── bronze/
│   ├── silver/
│   └── gold/
├── notebook/
├── src/
├── docker-compose.yml
├── Makefile
└── readme.md
```

## Key Files
1. **`docker-compose.yml`**: Defines services such as Spark, Airflow, LocalStack, and PostgreSQL, and how they communicate. Each container is configured with the necessary images and volumes to ensure environment functionality.
   
2. **`docker-entrypoint.sh`**: Initialization script that waits for the Airflow Webserver to be ready and starts the service, ensuring the environment is operational.

3. **`Dockerfile`**: Specifies how the Airflow image is built, including the installation of additional dependencies such as OpenJDK and the packages from `requirements.txt`.

4. **`Makefile`**: Automates Docker commands. The `Makefile` simplifies the process of building, starting, and stopping containers, eliminating the need for direct interaction with Docker commands.

5. **`.env`**: Found in various repository folders, these files store essential environment variables for Docker Compose execution. They contain critical information such as database access credentials, service configurations, and connection parameters. Docker Compose uses these variables to properly configure containers and enable service communication during pipeline execution.

>[!IMPORTANT]
>
>**AWS Variables**: The `.env` file related to LocalStack contains environment variables simulating AWS access credentials. These variables are used to create a local environment that mimics AWS, allowing testing of cloud service interactions, such as S3, without accessing a real AWS account. These credentials are fictitious and serve to enable service simulation on the LocalStack platform.

## LocalStack Dashboard Visualization

**Accessing the LocalStack Dashboard via app.localstack.cloud**:  
To facilitate monitoring and visualization of the simulated AWS services status in LocalStack, the project provides an online interface accessible at **[app.localstack.cloud](https://app.localstack.cloud)**. Upon accessing the platform, users can view detailed information about the AWS services being simulated in the local environment, such as S3, DynamoDB, among others.
  
In the **Status** section, users can see the current state of services, check if they are functioning correctly, or identify any simulation failures. This dashboard is useful to ensure all services operate as expected during development and testing.

![LocalStack Dashboard](./dashbord_localstack.png)

## Final Considerations
This project provides a robust and scalable solution for orchestrating and processing Big Data in an **on-premise environment**. Replacing SQLite with **PostgreSQL** in Airflow enhances storage capacity and scalability, making workflow orchestration more efficient. The use of **LocalStack** enables the simulation of key AWS services, such as **S3**, **SNS**, **SQS**, **DynamoDB**, **Lambda**, and **API Gateway**, facilitating the development and testing of cloud-dependent solutions. Automation provided by the `Makefile` and scripts ensures that any user can quickly set up the environment and start working with Big Data without difficulties.

