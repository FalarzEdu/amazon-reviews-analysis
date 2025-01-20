import os
from pymongo import MongoClient
from dotenv import load_dotenv

class Connection:
    def __init__(self):
        load_dotenv()

        # Initialize connection details
        self.mongo_host = os.getenv("MONGO_HOST", "localhost")
        self.mongo_port = int(os.getenv("MONGO_PORT", 27017))
        self.mongo_user = os.getenv("MONGO_USER")
        self.mongo_password = os.getenv("MONGO_PASSWORD")
        self.mongo_db = os.getenv("MONGO_DB", "test")
        self.client = None
        self.db = None

    def connect(self):
        """Establish connection to MongoDB."""
        try:
            self.client = MongoClient(
                host=self.mongo_host,
                port=self.mongo_port,
                username=self.mongo_user,
                password=self.mongo_password,
                authSource="admin"
            )
            self.db = self.client[self.mongo_db]
            print(f"Connected to MongoDB database: {self.mongo_db}")
            return self.db
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")
            return None

    def get_collection(self, collection_name):
        """Get a collection from the database."""
        if not self.db:
            print("No database connection found. Call connect() first.")
            return None
        return self.db[collection_name]

    def close(self):
        """Close the MongoDB connection."""
        if self.client:
            self.client.close()
            print("MongoDB connection closed.")
