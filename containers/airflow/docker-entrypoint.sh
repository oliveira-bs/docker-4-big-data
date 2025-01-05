#!/bin/bash
# Aguardar o Airflow Webserver
echo -e '\nWaiting for Airflow UI to be available on port 8080...'

while ! curl -s http://localhost:8080 > /dev/null; do
  sleep 2
done

echo -e 'Airflow UI is now available at http://localhost:8080!\n'

# Executar o Airflow Webserver
exec "$@"
