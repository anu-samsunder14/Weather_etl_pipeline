import os


def load_to_postgres(row,conn):
    print("DEBUG - Row being inserted:", row)
    cur = conn.cursor()
  
    cur.execute("""
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
    """)
    print("DEBUG - Row being inserted:", row)
    cur.execute("""
        INSERT INTO weather (city_name, temp_celsius, humidity, weather_description, obs_timestamp)
        VALUES (%(city_name)s, %(temp_celsius)s, %(humidity)s, %(weather_description)s, %(obs_timestamp)s)
        ON CONFLICT (city_name, obs_timestamp) DO NOTHING
    """, row)
    conn.commit()
    cur.close()
   
