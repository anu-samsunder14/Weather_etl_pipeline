# Weather ETL Pipeline

## Project Overview
This project is an **ETL (Extract, Transform, Load)** pipeline that automatically fetches live weather data for selected cities using the **OpenWeatherMap API**, transforms it into a structured format, and loads it into a **PostgreSQL database** — all orchestrated using **Apache Airflow** running inside **Docker containers**.

The DAG runs every 5 minutes and collects weather data for predefined Indian cities (e.g., Bengaluru, Mumbai).  

## Prerequisites
- Docker and Docker Compose installed  
- Python 3.x  
- Apache Airflow  
- PostgreSQL

This project demonstrates how to build a **data engineering pipeline** using **Apache Airflow** to automate the collection of weather data.

Every 5 minutes, the pipeline:
1. **Extracts** weather data from the OpenWeatherMap API for multiple cities.
2. **Transforms** the JSON response into a structured format.
3. **Loads** the cleaned data into a **PostgreSQL** database.


## Data Pipeline
<img width="1137" height="594" alt="Weather_etl" src="https://github.com/user-attachments/assets/ff25f892-dbb9-4722-ac5d-67fbba39d6af" />


weather-etl-airflow/
├── dags/
│ ├── extract.py # Fetches weather data using OpenWeatherMap API
│ ├── transform.py # Transforms JSON to tabular format
│ ├── load.py # Loads data into PostgreSQL
│ ├── weather_etl_docker_dag.py # Airflow DAG definition
│
├── docker-compose.yaml # Airflow, Redis, and PostgreSQL setup
├── .env # Environment variables (API key, Airflow UID, etc.)
├── logs/ # Airflow logs
├── plugins/ # Custom plugins (if any)
└── README.md # Project documentation

1. Start Docker Containers
    Build and start the Airflow stack using Docker Compose:
        docker compose up -d
2. Once the containers are up, trigger the Airflow DAG, and it will smoothly commence the ETL process.

3. PostgreSQL Table Schema

  ```sql
    -- SQL script to create the weather table
    The ETL automatically creates a table named weather:
            CREATE TABLE IF NOT EXISTS weather (
            id SERIAL PRIMARY KEY,
            city_name TEXT,
            temp_celsius DOUBLE PRECISION,
            humidity INTEGER,
            weather_description TEXT,
            obs_timestamp TIMESTAMP,
            inserted_at TIMESTAMP DEFAULT now(),
            UNIQUE(city_name, obs_timestamp)
        )
  ```

4. The data is successfully uploaded to your PostgreSQL database.

<img width="1169" height="244" alt="image" src="https://github.com/user-attachments/assets/83bd4c18-e52c-4938-93de-bf51a790ccde" />


