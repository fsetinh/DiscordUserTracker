import mariadb
import sys


def connect(user: str, pwd: str, host: str, database: str, port: int = 3306):
    try:
        conn = mariadb.connect(
            user=user,
            password=pwd,
            host=host,
            port=port,
            database=database
        )
        # print("Connected to MariaDB")
        return conn
    except mariadb.Error as e:
        # print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

def exe(command: str, extra = None):
    conn = connect('', '', '', '')
    cur = conn.cursor()
    try:
        cur.execute(command, extra)

        if command.strip().lower().startswith('select'):
            result = cur.fetchall()
        else:
            conn.commit()
            result = None

        return result

    except mariadb.Error as e:
        print(f"Error executing command: {command} | {e}")
        return None
    finally:
        cur.close()
        conn.close()
        # print("Connection to MariaDB was closed")