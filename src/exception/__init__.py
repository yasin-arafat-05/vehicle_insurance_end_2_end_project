import sys 
import logging

def error_message_details(error:Exception,error_details:sys)->str:
    """
    Description: Extracts detailed error information including filename, line number and error
    message

    Args:
        error (Exception): that exception occured
        error_details (sys): sys module to extract traceback error.

    Returns:
        str: A formated error message string
    """
    
    # extract traceback error:
    _,_,exc_tb = error_details.exc_info()
    
    # extract the file name:
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    # extract the line number and the error:
    line_number= exc_tb.tb_lineno
    error_message = f"Error occured in python script: [{file_name}] at line number: [{line_number}] : {str(error)}"
    
    # log this error:
    logging.error(error_message)
    return error_message



# Now for the parameter Error create a custom error:
class MyException(Exception):
    """
    Description: Custom exception class for handling error
    """
    def __init__(self,error_message:str,error_details:sys):
        """
        Descritption: Constructor for MyExceptoin Class
        Args:
            error_message (str): Error message
            error_details (sys): Extract Trackbook with sys module
        """
        super().__init__(error_message)
        self.error_message = error_message_details(error_message,error_details)
    
    def __str__(self):
        """
        Description: Convert string into error message
        Returns:
            _type_: error message
        """
        return self.error_message
    
    