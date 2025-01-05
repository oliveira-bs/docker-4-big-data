from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("DockerSparkApp") \
        .config("spark.local.dir", "/opt/airflow/data/spark-temp") \
        .config("spark.hadoop.fs.permissions.umask-mode", "000") \
        .getOrCreate()

    # Exemplo: Lendo dados de um arquivo CSV
    df = spark.read.csv("/opt/airflow/data/input/input_data.csv",
                        header=True, inferSchema=True)
    df.show()

    # Salvando dados processados
    df.write\
        .mode("overwrite")\
        .csv("/opt/airflow/data/output/processed")

    spark.stop()
