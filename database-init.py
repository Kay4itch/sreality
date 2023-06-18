from database import conn

print("Database opened successfully")
print("Initializing database")

cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS "flats" (
        id SERIAL PRIMARY KEY,
        seznam_id BIGINT NOT NULL,
        title VARCHAR(255) NOT NULL,
        image VARCHAR(255) NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(seznam_id)
    )
''')
conn.commit()
cursor.close()

print("Database successfully initialized")

