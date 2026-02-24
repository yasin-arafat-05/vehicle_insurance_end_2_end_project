import os
import sys
import json

import pandas as pd
from pandas import DataFrame

from src.logger import logging
from src.constants import CONFIG
from src.exception import MyException
from src.utils.main_utils import read_yaml_file
from src.entity.config_entity import DataValidationConfig
from src.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact


class DataValidation:
    def __init__(self, data_ingestion_artifact: DataIngestionArtifact, data_validation_config: DataValidationConfig):
        """
        Descriptions:  Datavalidation class instructor
        
        Args:
             data_ingestion_artifact: Output reference of data ingestion artifact stage
             data_validation_config: configuration for data validation
        """
        try:
            # with out the artifact of data ingestion we can't go forward
            self.data_ingestion_artifact = data_ingestion_artifact
            # data validation 
            self.data_validation_config = data_validation_config
            # read the yml file:
            self._schema_config =read_yaml_file(file_path=CONFIG.SCHEMA_FILE_PATH)
        except Exception as e:
            raise MyException(e,sys)
        

    def validate_number_of_columns(self, dataframe: DataFrame) -> bool:
        """
        Discriptions:  This method validates the number of columns 
        
        Args:
            dataframe (DataFrame): Dataframe of our data train and test data.
        
        Output:
            Returns bool value based on validation results
            
        Raises:
            Write an exception log and then raise an exception
        """
        try:
            status = len(dataframe.columns) == len(self._schema_config["columns"])
            logging.info(f"Is required column present: [{status}]")
            return status
        except Exception as e:
            raise MyException(e, sys)
        

    def is_column_exist(self, df: DataFrame) -> bool:
        """
        Description:  This method validates the existence of a numerical and categorical columns
        
        Args:
            dataframe (DataFrame): Dataframe of our data train or test data.
        
        Output:
            Returns bool value based on validation results.
            
        Raises: 
            Write an exception log and then raise an exception.
        """
        try:
            dataframe_columns = df.columns
            missing_numerical_columns = []
            missing_categorical_columns = []
            
            # from the yml file read the numerical_columns
            for column in self._schema_config["numerical_columns"]:
                if column not in dataframe_columns:
                    missing_numerical_columns.append(column)

            if len(missing_numerical_columns)>0:
                logging.info(f"Missing numerical column: {missing_numerical_columns}")

            # from the yml file read the categorical columns:
            for column in self._schema_config["categorical_columns"]:
                if column not in dataframe_columns:
                    missing_categorical_columns.append(column)

            if len(missing_categorical_columns)>0:
                logging.info(f"Missing categorical column: {missing_categorical_columns}")

            return False if len(missing_categorical_columns)>0 or len(missing_numerical_columns)>0 else True
        except Exception as e:
            raise MyException(e, sys) from e


    @staticmethod
    def read_data(file_path) -> DataFrame:
        """
        Discription: read csv file 
        Args:
            file_path (str): file path

        Raises:
            MyException: Write an exception and 

        Returns:
            DataFrame: Pandas DataFrame
        """
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise MyException(e, sys)
        

    def initiate_data_validation(self) -> DataValidationArtifact:
        """
        Description :   This method initiates the data validation component for the pipeline
        
        Args:
            self
            
        Output:
            Returns bool value based on validation results
            
        Raises:
            Write an exception log and then raise an exception
        """
        try:
            validation_error_msg = ""
            logging.info("Starting data validation")
            train_df, test_df = (DataValidation.read_data(file_path=self.data_ingestion_artifact.trained_file_path),
                                 DataValidation.read_data(file_path=self.data_ingestion_artifact.test_file_path))


            # === 1. Checking col len of dataframe for train/test df ===
            status = self.validate_number_of_columns(dataframe=train_df)
            if not status:
                validation_error_msg += f"Columns are missing in training dataframe. "
            else:
                logging.info(f"All required columns present in training dataframe: {status}")

            status = self.validate_number_of_columns(dataframe=test_df)
            if not status:
                validation_error_msg += f"Columns are missing in test dataframe. "
            else:
                logging.info(f"All required columns present in testing dataframe: {status}")


            # === 2. Validating col dtype for train/test df ===
            status = self.is_column_exist(df=train_df)
            if not status:
                validation_error_msg += f"Columns are missing in training dataframe. "
            else:
                logging.info(f"All categorical/int columns present in training dataframe: {status}")

            status = self.is_column_exist(df=test_df)
            if not status:
                validation_error_msg += f"Columns are missing in test dataframe."
            else:
                logging.info(f"All categorical/int columns present in testing dataframe: {status}")

            
            
            # === 3. If len(0)==0 that's mean no error return True ===
            validation_status = len(validation_error_msg) == 0
            data_validation_artifact = DataValidationArtifact(
                validation_status=validation_status,
                message=validation_error_msg,
                validation_report_file_path=self.data_validation_config.validation_report_file_path
            )
            

            # == 4. Ensure the directory for validation_report_file_path exists ===
            report_dir = os.path.dirname(self.data_validation_config.validation_report_file_path)
            os.makedirs(report_dir, exist_ok=True)

            # ===5.  Save validation status and message to a JSON file ===
            validation_report = {
                "validation_status": validation_status,
                "message": validation_error_msg.strip()
            }

            with open(self.data_validation_config.validation_report_file_path, "w") as report_file:
                json.dump(validation_report, report_file, indent=4)
            logging.info("Data validation artifact created and saved to JSON file.")
            logging.info(f"Data validation artifact: {data_validation_artifact}")
            return data_validation_artifact
        except Exception as e:
            raise MyException(e, sys) from e