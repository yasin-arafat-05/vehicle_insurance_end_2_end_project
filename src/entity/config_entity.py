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
    

# ========3. DataValidation Data Holder =========
@dataclass
class DataValidationConfig:
    data_validation_dir: str = os.path.join(training_pipeline_config.artifact_dir, CONFIG.DATA_VALIDATION_DIR_NAME)
    validation_report_file_path: str = os.path.join(data_validation_dir, CONFIG.DATA_VALIDATION_REPORT_FILE_NAME)


# ========4. DataValidation Data Holder =========
@dataclass
class DataTransformationConfig:
    data_transformation_dir: str = os.path.join(training_pipeline_config.artifact_dir, CONFIG.DATA_TRANSFORMATION_DIR_NAME)
    transformed_train_file_path: str = os.path.join(data_transformation_dir, CONFIG.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
                                                    CONFIG.TRAIN_FILE_NAME.replace("csv", "npy"))
    transformed_test_file_path: str = os.path.join(data_transformation_dir, CONFIG.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
                                                   CONFIG.TEST_FILE_NAME.replace("csv", "npy"))
    transformed_object_file_path: str = os.path.join(data_transformation_dir,
                                                     CONFIG.DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR,
                                                     CONFIG.PREPROCESSING_OBJECT_FILE_NAME)
    
# ========5. Model Tranning Data Holder =========
@dataclass
class ModelTrainerConfig:
    model_trainer_dir: str = os.path.join(training_pipeline_config.artifact_dir, CONFIG.MODEL_TRAINER_DIR_NAME)
    trained_model_file_path: str = os.path.join(model_trainer_dir, CONFIG.MODEL_TRAINER_TRAINED_MODEL_DIR, CONFIG.MODEL_FILE_NAME)
    expected_accuracy: float = CONFIG.MODEL_TRAINER_EXPECTED_SCORE
    model_config_file_path: str = CONFIG.MODEL_TRAINER_MODEL_CONFIG_FILE_PATH
    
    _dt_criterion : str = CONFIG.MODEL_DT_CRITERION
    _dt_max_depth : int = CONFIG.MODEL_DT_MAX_DEPTH
    _dt_min_samples_leaf : int = CONFIG.MODEL_DT_MIN_SAMPLES_LEAF
    _dt_min_sample_split : int = CONFIG.MODEL_DT_MIN_SAMPLES_SPLIT

    _rf_criterion : str = CONFIG.MODEL_RF_CRITERION
    _rf_n_estimator : int = CONFIG.MODEL_RF_N_ESTIMATOR
    _rf_min_samples_split : int = CONFIG.MODEL_RF_MIN_SAMPLES_SPLIT
    