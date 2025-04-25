CREATE OR REPLACE FUNCTION search_by_pattern(pattern TEXT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT phone_book.id, phone_book.name, phone_book.phone
    FROM phone_book
    WHERE phone_book.name ILIKE '%' || pattern || '%'
       OR phone_book.phone LIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

-- Процедура для вставки/обновления пользователя
CREATE OR REPLACE PROCEDURE upsert_user(
    user_name VARCHAR,
    user_phone VARCHAR
)
AS $$
BEGIN
    UPDATE phone_book 
    SET phone = user_phone
    WHERE name = user_name;
    
    IF NOT FOUND THEN
        INSERT INTO phone_book(name, phone)
        VALUES(user_name, user_phone);
    END IF;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION is_valid_phone(phone VARCHAR)
RETURNS BOOLEAN AS $$
BEGIN
    RETURN phone ~ '^[0-9]{10,15}$'; -- Проверяем, что телефон состоит только из цифр (10-15 символов)
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE insert_many_users(
    IN users_data VARCHAR[][],
    OUT invalid_data VARCHAR[]
)
AS $$
DECLARE
    user_record VARCHAR[];
BEGIN
    invalid_data := '{}'; -- Инициализируем пустой массив для некорректных данных
    
    FOREACH user_record SLICE 1 IN ARRAY users_data
    LOOP
        IF array_length(user_record, 1) = 2 AND is_valid_phone(user_record[2]) THEN
            CALL upsert_user(user_record[1], user_record[2]);
        ELSE
            invalid_data := invalid_data || (user_record[1] || ',' || user_record[2]);
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_users_paginated(
    lim INTEGER,
    offs INTEGER
)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT phone_book.id, phone_book.name, phone_book.phone
    FROM phone_book
    ORDER BY name
    LIMIT lim
    OFFSET offs;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE delete_user(
    search_term VARCHAR
)
AS $$
BEGIN
    IF search_term ~ '^[0-9]+$' THEN
        DELETE FROM phone_book WHERE phone = search_term;
    ELSE
        DELETE FROM phone_book WHERE name = search_term;
    END IF;
END;
$$ LANGUAGE plpgsql;