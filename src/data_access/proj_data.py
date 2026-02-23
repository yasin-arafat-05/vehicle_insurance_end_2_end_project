""" 
Fetch Model Tranning data from MongoDB Database.
"""
import sys
import pandas as pd
import numpy as np
from typing import Optional

from src.constants import CONFIG
from src.exception import MyException
from src.configuration.mongo_db_connection import MongoDBClient

class ProjData:
    """
    Description: A class to export MongoDB records as a pandas DataFrame.
    """

    def __init__(self) -> None:
        """
        Description: Initializes the MongoDB client connection.
        """
        try:
            self.mongo_client = MongoDBClient(database_name=CONFIG.DATABASE_NAME)
        except Exception as e:
            raise MyException(e, sys)
        

    def export_collection_as_dataframe(self, collection_name: str, database_name: Optional[str] = None) -> pd.DataFrame:
        """
        Description: Exports an entire MongoDB collection as a pandas DataFrame.

        Args: 
        collection_name (str):  The name of the MongoDB collection to export.
        database_name (Optional[str])  Defaults to DATABASE_NAME.

        Returns:
          pd.DataFrame
            DataFrame containing the collection data, with '_id' column removed and 'na' values replaced with NaN.
        """
        try:
            # Access specified collection from the default or specified database
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]

            # Convert collection data to DataFrame and preprocess
            print("Fetching data from mongoDB")
            df = pd.DataFrame(list(collection.find()))
            print(f"Data fecthed with len: {len(df)}")
            if "id" in df.columns.to_list():
                df = df.drop(columns=["id"], axis=1)
            df.replace({"na":np.nan},inplace=True)
            return df

        except Exception as e:
            raise MyException(e, sys)