import psycopg2
import os


local_db = 'postgresql://postgres:postgres@localhost:5432/fleetnav'

if os.environ['FLASK_ENV'] == 'development':
    postgres_uri = local_db
    def get_db():
        conn = psycopg2.connect(database="fleetnav", 
                                user="postgres", 
                                password="postgres", 
                                host="localhost", 
                                port="5432")
        return conn
else:
    prod_db = os.environ['SQLALCHEMY_DATABASE_URI']
    postgres_uri = prod_db

    prod_user = prod_db[13:].split(':')[0]
    prod_pwd = prod_db[13:].split(':')[1].split('@')[0]
    prod_host = prod_db[13:].split(':')[1].split('@')[1]
    prod_dbname = prod_db[13:].split(':')[2].split('/')[1]
    def get_db():
        conn = psycopg2.connect(database=prod_dbname, 
                                user=prod_user, 
                                password=prod_pwd, 
                                host=prod_host, 
                                port="5432")
        return conn



