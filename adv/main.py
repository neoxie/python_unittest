import business
import database


def main():
    mongo_database = database.MongoDatabase()
    result = business.query_db(mongo_database, 'test', 'students')
    print(result)


if __name__ == "__main__":
    main()
