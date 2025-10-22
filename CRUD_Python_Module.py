from pymongo import MongoClient

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database and the animals collection. 
        # 
        # NOTE: Authentication is disabled on this MongoDB instance, so
        # username/password are not used.
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 

        self.client = MongoClient('mongodb://%s:%d/' % (HOST, PORT))
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if data is not None: 
            self.collection.insert_one(data)              
            return True
        else: 
            raise Exception("Nothing to save, because data parameter is empty") 

    # Create method to implement the R in CRUD. 
    def read(self, query):
        if query is not None and isinstance(query, dict):
            cursor = self.collection.find(query)
            return list(cursor)
        else:
            raise Exception("Query parameter is empty or not a dictionary")
    # Update method to implement the U in CRUD.
    def update(self, query, new_values):
        if query is not None and isinstance(query, dict):
            if new_values is not None and isinstance(new_values, dict):
                result = self.collection.update_many(query, {"$set": new_values})
                return result.modified_count    # number of documents updated
            else:
                raise Exception("new_values parameter is empty or not a dictionary")
        else:
            raise Exception("query parameter is empty or not a dictionary")

    # Delete method to implement the D in CRUD.
    def delete(self, query):
        if query is not None and isinstance(query, dict):
            result = self.collection.delete_many(query)
            return result.deleted_count        # number of documents deleted
        else:
            raise Exception("query parameter is empty or not a dictionary")
