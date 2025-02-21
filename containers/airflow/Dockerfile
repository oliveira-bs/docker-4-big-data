FROM apache/airflow:2.10.4-python3.12

USER root
RUN apt-get update && \
    apt-get install nano && \
    apt-get install -y --no-install-recommends \
    openjdk-17-jre-headless \
    procps \
    curl \
    unzip && \
    apt-get autoremove -yqq --purge && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Download and install AWS CLI
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm -rf awscliv2.zip aws

USER airflow
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64

RUN pip install --upgrade pip

# Instalação de dependências adicionais
COPY requirements.txt .
RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt
