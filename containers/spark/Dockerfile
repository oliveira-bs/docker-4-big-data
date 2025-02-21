FROM bitnami/spark:3.5.4

USER root
# Instala pacotes necessários
RUN apt update && apt install -y curl unzip \
    && curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip && ./aws/install \
    && rm -rf awscliv2.zip aws

# # Verifica instalação
# RUN aws --version
