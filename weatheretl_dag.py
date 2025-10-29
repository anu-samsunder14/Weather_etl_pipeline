from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from extract import fetch_weather
from transform import transform_weather
from load import load_to_postgres
from airflow.providers.postgres.hooks.postgres import PostgresHook


default_args = {
    "owner": "airflow",
    "retries": 0,
    "retry_delay": timedelta(minutes=5)
}

def run_weather_etl():
    hook = PostgresHook(postgres_conn_id="postgres_default")  # 👈 use Airflow connection
    conn = hook.get_conn()
    
    cities = ["Bengaluru,IN", "Mumbai,IN"]
    for city in cities:
        data = fetch_weather(city)
        row = transform_weather(data)
        load_to_postgres(row,conn)
    conn.commit()
    
with DAG(
    dag_id="weather_etl_docker_dag",
    default_args=default_args,
    start_date=datetime(2025, 10, 25),
    schedule_interval="*/5 * * * *",
   # schedule_interval="@hourly",
    catchup=False,
    tags=["weather", "etl"]
) as dag:
    etl_task = PythonOperator(
        task_id="run_weather_etl",
        python_callable=run_weather_etl
    )
