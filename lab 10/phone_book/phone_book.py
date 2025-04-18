import psycopg2
import csv

def get_db_connection():
    return psycopg2.connect(
        host='localhost',
        database='postgres',
        user='postgres',
        password='123Bek'
    )

def import_from_csv():
    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        with open('phone_book.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if len(row) >= 2:
                    name, phone = row[0], row[1]
                    cur.execute(
                        "INSERT INTO phone_book (name, phone) VALUES (%s, %s) ON CONFLICT (phone) DO NOTHING",
                        (name, phone)
                    )
        conn.commit()
        print("Данные успешно импортированы из CSV!")
    except Exception as e:
        print(f"Ошибка при импорте: {e}")
    finally:
        cur.close()
        conn.close()

def add_user_console():
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    
    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        cur.execute(
            "INSERT INTO phone_book (name, phone) VALUES (%s, %s)",
            (name, phone)
        )
        conn.commit()
        print("Пользователь успешно добавлен!")
    except psycopg2.IntegrityError:
        print("Ошибка: такой телефон уже существует")
    finally:
        cur.close()
        conn.close()

def update_user():
    conn = get_db_connection()
    cur = conn.cursor()
    
    print("\n1. Изменить имя")
    print("2. Изменить телефон")
    choice = input("Выберите действие (1/2): ")
    
    if choice == '1':
        phone = input("Введите телефон пользователя: ")
        new_name = input("Введите новое имя: ")
        
        cur.execute(
            "UPDATE phone_book SET name = %s WHERE phone = %s",
            (new_name, phone)
        )
        if cur.rowcount == 0:
            print("Пользователь с таким телефоном не найден")
        else:
            conn.commit()
            print("Имя успешно обновлено!")
    
    elif choice == '2':
        name = input("Введите имя пользователя: ")
        new_phone = input("Введите новый телефон: ")
        
        try:
            cur.execute(
                "UPDATE phone_book SET phone = %s WHERE name = %s",
                (new_phone, name)
            )
            if cur.rowcount == 0:
                print("Пользователь с таким именем не найден")
            else:
                conn.commit()
                print("Телефон успешно обновлен!")
        except psycopg2.IntegrityError:
            print("Ошибка: такой телефон уже существует")
    
    cur.close()
    conn.close()

def query_data():
    conn = get_db_connection()
    cur = conn.cursor()
    
    print("\n1. Поиск по имени")
    print("2. Поиск по телефону")
    print("3. Показать все контакты")
    choice = input("Выберите действие (1/2/3): ")
    
    if choice == '1':
        name = input("Введите имя для поиска: ")
        cur.execute(
            "SELECT name, phone FROM phone_book WHERE name ILIKE %s",
            (f'%{name}%',)
        )
    elif choice == '2':
        phone = input("Введите телефон для поиска: ")
        cur.execute(
            "SELECT name, phone FROM phone_book WHERE phone LIKE %s",
            (f'%{phone}%',)
        )
    elif choice == '3':
        cur.execute("SELECT name, phone FROM phone_book ORDER BY name")
    
    results = cur.fetchall()
    if results:
        print("\nРезультаты поиска:")
        for name, phone in results:
            print(f"{name}: {phone}")
    else:
        print("Ничего не найдено")
    
    cur.close()
    conn.close()

def delete_user():
    conn = get_db_connection()
    cur = conn.cursor()
    
    print("\n1. Удалить по имени")
    print("2. Удалить по телефону")
    choice = input("Выберите действие (1/2): ")
    
    if choice == '1':
        name = input("Введите имя для удаления: ")
        cur.execute(
            "DELETE FROM phone_book WHERE name = %s RETURNING phone",
            (name,)
        )
    elif choice == '2':
        phone = input("Введите телефон для удаления: ")
        cur.execute(
            "DELETE FROM phone_book WHERE phone = %s RETURNING name",
            (phone,)
        )
    
    result = cur.fetchone()
    if result:
        conn.commit()
        print(f"Пользователь успешно удален: {result[0]}")
    else:
        print("Пользователь не найден")
    
    cur.close()
    conn.close()

def main():
    while True:
        print("\nТелефонная книга")
        print("1. Импорт из CSV")
        print("2. Добавить пользователя")
        print("3. Обновить данные")
        print("4. Поиск")
        print("5. Удалить")
        print("6. Выход")
        
        choice = input("Выберите действие (1-6): ")
        
        if choice == '1':
            import_from_csv()
        elif choice == '2':
            add_user_console()
        elif choice == '3':
            update_user()
        elif choice == '4':
            query_data()
        elif choice == '5':
            delete_user()
        elif choice == '6':
            break
        else:
            print("Неверный выбор")

if __name__ == '__main__':
    main()