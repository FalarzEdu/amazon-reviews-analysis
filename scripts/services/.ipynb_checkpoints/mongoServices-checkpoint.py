class MongoServices:
    def __init__(self, connection):
        self.connection = connection

    def readAll(self, collection_name):
        collection = self.connection[collection_name]
        return list(collection.find())
