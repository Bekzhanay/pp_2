import psycopg2
import csv
from typing import List, Tuple

class PhoneBook:
    def __init__(self):
        self.conn = psycopg2.connect(
            host='localhost',
            database='postgres',
            user='postgres',
            password='123Bek'
        )
        self.cur = self.conn.cursor()
        
        # Создаем таблицу
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS phone_book (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                phone VARCHAR(20) NOT NULL UNIQUE
            );
        """)
        self.conn.commit()
        
        self._create_functions()
    
    def _create_functions(self):
        
        try:
            with open('phonebook_functions.sql', 'r') as f:
                sql_script = f.read()
                self.cur.execute(sql_script)
                self.conn.commit()
        except Exception as e:
            print(f"Ошибка при создании функций: {e}")
            self.conn.rollback()
    
    def search_by_pattern(self, pattern: str) -> List[Tuple]:
        self.cur.callproc('search_by_pattern', (pattern,))
        return self.cur.fetchall()
    
    def upsert_user(self, name: str, phone: str) -> None:
        self.cur.callproc('upsert_user', (name, phone))
        self.conn.commit()
    
    def import_from_csv(self, filename: str) -> None:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            next(reader)  

            users_data = []
            for row in reader:
                if len(row) >= 2:
                    users_data.append([row[0], row[1]])
            
            # Вызываем процедуру массовой вставки
            self.cur.callproc('insert_many_users', (users_data, None))
            self.conn.commit()
            
            invalid_data = self.cur.fetchone()[0]
            if invalid_data:
                print("Некорректные данные:")
                for data in invalid_data:
                    print(data)
    
    def get_users_paginated(self, limit: int, offset: int) -> List[Tuple]:
        self.cur.callproc('get_users_paginated', (limit, offset))
        return self.cur.fetchall()
    
    def delete_user(self, search_term: str) -> bool:
        self.cur.callproc('delete_user', (search_term,))
        rows_deleted = self.cur.rowcount
        self.conn.commit()
        return rows_deleted > 0
    
    def close(self):
        self.cur.close()
        self.conn.close()

def main():
    pb = PhoneBook()
    
    while True:
        print("\nPhoneBook Management")
        print("1. Search by pattern")
        print("2. Add/update user")
        print("3. Import from CSV")
        print("4. List users with pagination")
        print("5. Delete user")
        print("6. Exit")
        
        choice = input("Select option (1-6): ")
        
        try:
            if choice == '1':
                pattern = input("Enter search pattern: ")
                results = pb.search_by_pattern(pattern)
                if results:
                    print("\nSearch results:")
                    for id, name, phone in results:
                        print(f"{id}: {name} - {phone}")
                else:
                    print("No results found.")
            
            elif choice == '2':
                name = input("Enter name: ")
                phone = input("Enter phone: ")
                pb.upsert_user(name, phone)
                print("Operation completed successfully!")
            
            elif choice == '3':
                filename = input("Enter CSV filename (default: phone_book.csv): ") or "phone_book.csv"
                pb.import_from_csv(filename)
                print("Import completed!")
            
            elif choice == '4':
                limit = int(input("Enter limit: "))
                offset = int(input("Enter offset: "))
                users = pb.get_users_paginated(limit, offset)
                if users:
                    print("\nUsers:")
                    for id, name, phone in users:
                        print(f"{id}: {name} - {phone}")
                else:
                    print("No more users.")
            
            elif choice == '5':
                search_term = input("Enter name or phone to delete: ")
                if pb.delete_user(search_term):
                    print("User deleted successfully!")
                else:
                    print("User not found.")
            
            elif choice == '6':
                break
            
            else:
                print("Invalid choice. Please try again.")
        
        except Exception as e:
            print(f"Error: {e}")
            pb.conn.rollback()
    
    pb.close()

if __name__ == '__main__':
    main()