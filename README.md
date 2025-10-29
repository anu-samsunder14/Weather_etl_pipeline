# ETL_Sales_Data

## Project Overview
This repository contains a mini project demonstrating ETL using Apache Airflow for orchestration.

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
