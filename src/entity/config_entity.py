import os 
from datetime import datetime
from src.constants import CONFIG
from dataclasses import dataclass


TIMESTAMP : str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")


# ========1. Tranning Pipeline Data Holder =========
@dataclass
class TrainingPipelineConfig:
    pipeline_name: str = CONFIG.PIPELINE_NAME 
    artifact_dir: str = CONFIG.ARTIFACT_DIR
    timestamp: str = TIMESTAMP
    
training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig()


# ========2. DataIngestion Data Holder =========
@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(training_pipeline_config.artifact_dir, CONFIG.DATA_INGESTION_DIR_NAME)
    feature_store_file_path: str = os.path.join(data_ingestion_dir, CONFIG.DATA_INGESTION_FEATURE_STORE_DIR, CONFIG.FILE_NAME)
    training_file_path: str = os.path.join(data_ingestion_dir, CONFIG.DATA_INGESTION_INGESTED_DIR, CONFIG.TRAIN_FILE_NAME)
    testing_file_path: str = os.path.join(data_ingestion_dir, CONFIG.DATA_INGESTION_INGESTED_DIR, CONFIG.TEST_FILE_NAME)
    train_test_split_ratio: float = CONFIG.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
    collection_name:str = CONFIG.DATA_INGESTION_COLLECTION_NAME
    