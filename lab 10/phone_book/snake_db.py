import psycopg2

def get_db_connection():
    return psycopg2.connect(
        host='localhost',
        database='postgres',
        user='postgres',
        password='123Bek'
    )

def get_user(username):
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute(
        "SELECT id, current_level, highest_score FROM snake_users WHERE username = %s",
        (username,)
    )
    user = cur.fetchone()
    
    cur.close()
    conn.close()
    
    if user:
        return {
            'id': user[0],
            'level': user[1],
            'highest_score': user[2]
        }
    return None

def create_user(username):
    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        cur.execute(
            "INSERT INTO snake_users (username) VALUES (%s) RETURNING id",
            (username,)
        )
        user_id = cur.fetchone()[0]
        conn.commit()
        return {'id': user_id, 'level': 1, 'highest_score': 0}
    except psycopg2.IntegrityError:
        print("Пользователь уже существует")
        return None
    finally:
        cur.close()
        conn.close()

def save_game(user_id, score, level):
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute("""
    UPDATE snake_users 
    SET current_level = %s,
        highest_score = GREATEST(highest_score, %s)
    WHERE id = %s
    """, (level, score, user_id))
    
    cur.execute("""
    INSERT INTO snake_scores (user_id, score, level)
    VALUES (%s, %s, %s)
    """, (user_id, score, level))
    
    conn.commit()
    cur.close()
    conn.close()
    print("Игра сохранена!")