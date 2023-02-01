import mariadb
import dbcreds

def connect_db():
    try:
        conn = mariadb.connect(
        user = dbcreds.user,
        password = dbcreds.password,
        host = dbcreds.host,
        port = dbcreds.port,
        database = dbcreds.database,
        autocommit=True
        )
        cursor = conn.cursor()
        return cursor
    except mariadb.OperationalError as e:
        print("Could not connect to the database", e)
    except Exception as e:
        print("Something went wrong")

def execute_statement(cursor, statement, args=[]):
    try:
        cursor.execute(statement, args)
        result = cursor.fetchall()
        return result
    # except mariadb.IntegrityError as e:
    #     if "error" in e.msg:
    #         print("complete this later")
    #     elif "other error" in e.msg:
    #         print("complete this later.")
    #     else:
    #         print("Data was not valid:", e)
    # except mariadb.ProgrammingError as e:
    #     if "doesn't have a result set" in e.msg:
            # means if this happens, don't worry about it, i'm not returning anything. it's an insert statement, not a select statement.
        #     return None
        # else:
        #     print("syntax error probably", e)
    # except mariadb.OperationalError as e:
    #     print("Something went wrong with the connection to the DB")
    except Exception as e:
        print("Something ain't correct:",e)
    
def close_connection(cursor):
    try:
        conn = cursor.connection
        cursor.close()
        conn.close()
    except mariadb.OperationalError:
        print("OPERATIONAL ERROR: ")
    except Exception:
        print("Something went wrong when closing the connection")

def run_statement(statement, args=[]):
    cursor = connect_db()
    if cursor == None:
        return None
    results = execute_statement(cursor, statement, args={})
    if (results == None):
        return None
    close_connection(cursor)
    return results