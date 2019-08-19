from database import *


def query_db(db, database_name, table_name):
    return db.execute(database_name, table_name)
