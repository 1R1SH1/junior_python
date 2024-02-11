import psycopg2
from config import host, user, password, db_name

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            """Drop Table file_versions CASCADE"""
        )

    with connection.cursor() as cursor:
        cursor.execute(
            """Drop Table projects CASCADE"""
        )

    with connection.cursor() as cursor:
        cursor.execute(
            """Drop Table values CASCADE"""
        )

    with connection.cursor() as cursor:
        cursor.execute(
            """Create Table file_versions(
                id int Primary Key,
                version varchar(50) Not NULL,
                file_name varchar(50));"""
        )

    with connection.cursor() as cursor:
        cursor.execute(
            """Create Table projects(
                id int Primary Key,
                code int Not NULL,
                name varchar(100));"""
        )

    with connection.cursor() as cursor:
        cursor.execute(
            """Create Table values(
                id int Primary Key,
                project_id int REFERENCES projects (id),
                file_version_id int REFERENCES file_versions (id),
                date date,
                plan serial,
                fact serial);"""
        )

    with connection.cursor() as cursor:
        cursor.execute(
            """Insert Into file_versions (id, version, file_name)
            Values (1, 'Проект 1', 'Проект 1');"""
        )

    with connection.cursor() as cursor:
        cursor.execute(
            """Insert Into projects (id, code, name)
            Values (1, '567', 'Проект 1');"""
        )

    with connection.cursor() as cursor:
        cursor.execute(
            """Insert Into values (id, date, plan, fact)
            Values (1, '11/02/2024', 5.5, 4.54);"""
        )



except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
