FROM apache/airflow:2.10.4-python3.12

USER root
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    openjdk-17-jre-headless \
    procps \
    curl && \
    apt-get autoremove -yqq --purge && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER airflow
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64

RUN pip install --upgrade pip

# Instalação de dependências adicionais
COPY requirements.txt .
RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt
