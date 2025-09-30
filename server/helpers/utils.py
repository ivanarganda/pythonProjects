def get_queries():

    try:
        
        return { 
            "create_roles_table": """
                CREATE TABLE IF NOT EXISTS roles ( 
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    role TEXT NOT NULL
                )
            """,
            "init_roles_data": """
                INSERT OR IGNORE INTO roles (role)
                    SELECT 'admin'
                    WHERE NOT EXISTS (SELECT 1 FROM roles WHERE role = 'admin')
                    UNION
                    SELECT 'admin2'
                    WHERE NOT EXISTS (SELECT 1 FROM roles WHERE role = 'admin2')
                    UNION
                    SELECT 'user'
                    WHERE NOT EXISTS (SELECT 1 FROM roles WHERE role = 'user')
            """,
            "create_users_table": """ 
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    password TEXT NOT NULL,
                    role INTEGER,
                    FOREIGN KEY (role) REFERENCES roles(id) ON DELETE CASCADE
                )
            """,
            "init_user_admin_data": """
                INSERT INTO users (name, password, role)
                    SELECT ?, ?, 1
                    WHERE NOT EXISTS (
                        SELECT 1 FROM users WHERE name = 'ivan'
                    )
            """
        }

    except ( KeyError, TypeError ):
        return False