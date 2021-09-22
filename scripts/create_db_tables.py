import pandas as pd
import mysql.connector as mysql

# from decouple import config
#
# mysql_user, mysql_pass = config('mysql_user'), config('mysql_pass')
# print(postgres_user, postgres_pass)

def DBConnect(dbName=None):
    """

    Parameters
    ----------
    dbName :
        Default value = None)

    Returns
    -------

    """
    try:
        conn = mysql.connect(host="localhost",
                             user="root",
                             passwd="password",
                             port="3306"
                             )

        cur = conn.cursor()
        conn.autocommit = True
        print('Connection Established')

    except Exception as error:
        print(error)
        conn, cur = None, None

    return conn, cur


def createDB(dbName: str) -> None:
    """

    Parameters
    ----------
    dbName :
        str:
    dbName :
        str:
    dbName:str :


    Returns
    -------

    """
    try:

        conn, cur = DBConnect()
        sql = f"CREATE DATABASE {dbName};"
        cur.execute(sql)
        # conn.commit()
        cur.close()

    except Exception as e:
        print("::::", e)

def createTables(dbName: str) -> None:
    """

    Parameters
    ----------
    dbName :
        str:
    dbName :
        str:
    dbName:str :


    Returns
    -------

    """
    conn, cur = DBConnect(dbName)
    sqlFile = './sql_schema/table_schema.sql'
    fd = open(sqlFile, 'r')
    readSqlFile = fd.read()
    fd.close()

    sqlCommands = readSqlFile.split(';')

    for command in sqlCommands:
        try:
            res = cur.execute(command)
            response = "Table created sucessfuly"
        except Exception as ex:
            print("Command skipped: ", command)
            response = "Table Not Created"
            print(ex)
    conn.commit()
    cur.close()

    return print(response)


if __name__ == "__main__":
    createDB(dbName='sensor_data')
    createTables(dbName='sensor_data')
    print("Sucessfully, created db and Tables")