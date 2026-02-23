
# ======1. Check logging working or not =========
# from src.logger import logging
# logging.debug("This is a debug message for testing purpose.")
# logging.info("This is a info message for testing purpuse.")


# ======2. Check exception code working or not =========
# import sys 
# from src.logger import logging
# from src.exception import MyException

# try: 
#     a = 1 + 'Z'
# except Exception as e:
#     logging.info(e)
#     raise MyException(e,sys) from e 


    
# ======3. Test the pipeline from data ingestion =========
from src.pipline.training_pipeline import TrainPipeline

pipeline = TrainPipeline()
pipeline.run_pipeline()
