""" 
Some utility function:
- Read Yaml File
- Write Yaml File 
- 
"""
import os
import sys
import dill
import yaml
import numpy as np
from pandas import DataFrame
from src.logger import logging
from src.exception import MyException



# =============== 1. Read Yaml File =================
def read_yaml_file(file_path: str) -> dict:
    """
    Discription: This function read Yaml File.
    
    Args:
        file_path (str): File path of an yaml file.
    Raises:
        MyException: Custom Exception is not yaml or path or valid.
    Returns:
        dict: yaml file
    """
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise MyException(e, sys) from e


# =============== 2. Write Yaml File =================
def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    """
    Discription: Saving a yaml file.
    
    Args:
        file_path (str): File path of the ymal file.
        content (object): Content that will yml file will contain.
        replace (bool, optional): Will replacement. Defaults to False.
    Raises:
        MyException (custom exception).
    """
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content, file)
    except Exception as e:
        raise MyException(e, sys) from e


# ============== 3. Load File/Model/Object =================
def load_object(file_path: str) -> object:
    """
    Discription: Returns model/object from project directory.
    
    Args:
        file_path (str):  location of file to load
        
    Return:
        Model/Obj
    """
    try:
        with open(file_path, "rb") as file_obj:
            obj = dill.load(file_obj)
        return obj
    except Exception as e:
        raise MyException(e, sys) from e



# =============== 4. Save Numpy Array Data=================
def save_numpy_array_data(file_path: str, array: np.array):
    """
    Descriptions: Save numpy array data to file.
    
    Args:
        file_path: str location of file to save
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise MyException(e, sys) from e



# =============== 5. Load Numpy Array Data=================
def load_numpy_array_data(file_path: str) -> np.array:
    """
    Discription:  load numpy array data from file
    
    Args:
        file_path (str): location of file to load
        
    Returns:
        np.array data loaded
    """
    try:
        with open(file_path, 'rb') as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise MyException(e, sys) from e


# ============== 6. Load File/Model/Object =================
def save_object(file_path: str, obj: object) -> None:
    """
    Description: Save Object like model file.

    Args:
        file_path (str): File path
        obj (object): Objcet that we want to save

    Raises:
        MyException: custom error is failed
    """
    logging.info("Entered the save_object method of utils")

    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

        logging.info("Exited the save_object method of utils")

    except Exception as e:
        raise MyException(e, sys) from e



# def drop_columns(df: DataFrame, cols: list)-> DataFrame:

#     """
#     drop the columns form a pandas DataFrame
#     df: pandas DataFrame
#     cols: list of columns to be dropped
#     """
#     logging.info("Entered drop_columns methon of utils")

#     try:
#         df = df.drop(columns=cols, axis=1)

#         logging.info("Exited the drop_columns method of utils")
        
#         return df
#     except Exception as e:
#         raise MyException(e, sys) from e