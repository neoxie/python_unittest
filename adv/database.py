from abc import ABCMeta, abstractmethod
import pymongo


class BaseDatabase(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, database_name, table_name):
        pass


class MongoDatabase(BaseDatabase):
    def execute(self, database_name, table_name):
        client = pymongo.MongoClient(host='localhost', port=27017)
        database = client[database_name]
        collection = database[table_name]
        result = []
        for student in collection.find():
            result.append(student)

        return result


class DummyDatabase(BaseDatabase):
    def execute(self, database_name, table_name):
        return [{
            'id': '20170101',
            'name': 'Jordan',
            'age': 20,
            'gender': 'male'
        }, {
            'id': '20170202',
            'name': 'Mike',
            'age': 21,
            'gender': 'male'
        }]
