    Create Table file_versions(
        id int Primary Key,
        version varchar(50) Not NULL,
        file_name varchar(50)
    )

    Create Table projects(
        id int Primary Key,
        code int Not NULL,
        name varchar(100)
    )

    Create Table values(
        id int Primary Key,
        project_id int REFERENCES projects (id),
        file_version_id int REFERENCES file_versions (id),
        date date,
        plan serial,
        fact serial
    )