import pymongo

class Singleton(type):
    """
    Define an Instance operation that lets clients access its unique
    instance.
    """

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class ConnMongo(metaclass=Singleton):
    """
    Connection to MongoDB database
    """
    def conn(self):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["REGIE"]
        return mydb