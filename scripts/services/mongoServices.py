import logging

logging.basicConfig(level=logging.INFO)

class MongoServices:
    def __init__(self, connection):
        self.connection = connection

    ### CREATE
    def insert_document(self, collection, data):
        try:
            collection_name = collection.name
            logging.info(f"Inserting data into '{collection_name}'")
            
            if isinstance(data, dict) and "id" in data:
                result = collection.insert_one(data)
            elif isinstance(data, dict):
                result = collection.insert_many(list(data.values()))
            elif isinstance(data, list):
                result = collection.insert_many(data)
            else:
                raise ValueError("Data must be a single document (dict), list of documents, or dict of documents")
            
            logging.info(f"Data inserted into '{collection_name}' successfully.")
            return result
        except Exception as e:
            logging.error(f"Error inserting data into '{collection_name}': {e}")
            return None

    ### READ
    def read_all(self, collection):
        try:
            collection_name = collection.name
            logging.info(f"Reading all documents from collection '{collection_name}'")
            return list(collection.find())
        except Exception as e:
            logging.error(f"Error reading from collection '{collection_name}': {e}")
            return []

    def filtered_read(self, collection, filter):
        try:
            collection_name = collection.name
            logging.info(f"Filtering document(s) matching filter '{filter}' in '{collection_name}'")

            result = collection.find(filter)

            result_list = list(result)
            logging.info(f"Found {len(result_list)} document(s).")
            return result_list
        except Exception as e:
            logging.error(f"Error finding document(s) in '{collection_name}': {e}")
            return None

    ### UPDATE
    def update_document(self, collection, filter, data):
        try:
            collection_name = collection.name
            logging.info(f"Updating document(s) matching filter '{filter}' in '{collection_name}'")

            if not isinstance(data, dict):
                raise ValueError("Data must be a dictionary containing the fields to update.")

            result = collection.update_many(filter, {"$set": data})

            logging.info(f"Matched {result.matched_count} document(s), updated {result.modified_count} document(s).")
            return result
        except Exception as e:
            logging.error(f"Error updating document(s) in '{collection_name}': {e}")
            return None

    ### DELETE
    def delete_document(self, collection, filter):
        try:
            collection_name = collection.name
            logging.info(f"Deleting document(s) matching filter '{filter}' in '{collection_name}'")

            result = collection.delete_many(filter)

            logging.info(f"Removed {result.deleted_count} document(s).")
            return result
        except Exception as e:
            logging.error(f"Error deleting document(s) in '{collection_name}': {e}")
            return None