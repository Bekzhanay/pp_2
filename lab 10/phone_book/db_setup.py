import psycopg2

def create_tables():
    conn = psycopg2.connect(
        host='localhost',
        database='postgres',
        user='postgres',
        password='123Bek'
    )
    cur = conn.cursor()
    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS phone_book (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        phone VARCHAR(20) NOT NULL UNIQUE
    );
    """)
    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS snake_users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(20) NOT NULL UNIQUE,
        current_level INT DEFAULT 1,
        highest_score INT DEFAULT 0
    );
    """)
    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS snake_scores (
        id SERIAL PRIMARY KEY,
        user_id INT REFERENCES snake_users(id),
        score INT NOT NULL,
        level INT NOT NULL,
        saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    
    conn.commit()
    cur.close()
    conn.close()
    print("Tables created successfully!")

if __name__ == '__main__':
    create_tables()