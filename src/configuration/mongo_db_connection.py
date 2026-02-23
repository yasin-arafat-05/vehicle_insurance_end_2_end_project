import os
import sys
import pymongo
import certifi

from src.logger import logging
from src.constants import CONFIG
from src.exception import MyException


# Load the certificate authority file to avoid timeout errors when connecting to MongoDB
ca = certifi.where()


class MongoDBClient:
    """
    Description:  Establishing a connection to the MongoDB database.
    
    Methods:
        __init__(database_name: str) -> None
            Initializes the MongoDB connection using the given database name.
    """
    # Shared MongoClient instance across all MongoDBClient instances
    client = None  

    def __init__(self, database_name: str = CONFIG.DATABASE_NAME) -> None:
        """
        Description: Initializes a connection to the MongoDB database. If no existing connection is found, it establishes a new one.
        
        Args:
            database_name (str, optional): DATABASE_NAME Of MongoDB.

        Raises:
            MyException: Custom Exception
            If there is an issue connecting to MongoDB or if the environment variable for the MongoDB URL is not set.
        """
        try:
            # Check if a MongoDB client connection has already been established; if not, create a new one
            if MongoDBClient.client is None:
                mongo_db_url = CONFIG.MONGODB_URL 
                if mongo_db_url is None:
                    raise Exception(f"Environment variable '{CONFIG.MONGODB_URL}' is not set.")
                # Establish a new MongoDB client connection
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
                
            # Use the shared MongoClient for this instance
            self.client = MongoDBClient.client
            self.database = self.client[database_name]  
            self.database_name = database_name
            logging.info("MongoDB connection successful.")
            
        except Exception as e:
            raise MyException(e, sys)
        