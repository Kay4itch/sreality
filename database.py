import psycopg2
import time

max_tries = 10
tries = 0
while tries < max_tries:
    tries += 1
    try:
        conn = psycopg2.connect(
            host="postgres",
            database="postgres",
            user="postgres",
            password="postgres"
        )
    except psycopg2.OperationalError:
        print("Database connection failed. It's probably not ready yet. Retrying in 1s...")
        time.sleep(1)
