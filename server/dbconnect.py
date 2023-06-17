# import pymysql
import psycopg2

# def connection():
#     config = pymysql.connect (
#             user = 'root',
#            password = 'root',
#            host = 'localhost',
#            database =  'movie_rec',
#             )
#     a = config.cursor()
#     return a, config


def connection():
    config = psycopg2.connect(
        user='username',
        password='password',
        host='localhost',
        database='database_name',
    )
    cursor = config.cursor()
    return cursor, config


