import os
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # ===============================
    # MongoDB Configuration
    # ===============================
    MONGODB_USER : str 
    MONGODB_PASSWORD : str 
    DATABASE_NAME: str
    COLLECTION_NAME: str
    MONGODB_URL: str

    # ===============================
    # Pipeline & Artifact
    # ===============================
    PIPELINE_NAME: str
    ARTIFACT_DIR: str

    # ===============================
    # File Names
    # ===============================
    MODEL_FILE_NAME: str
    TARGET_COLUMN: str
    CURRENT_YEAR: int
    PREPROCESSING_OBJECT_FILE_NAME: str

    FILE_NAME: str
    TRAIN_FILE_NAME: str
    TEST_FILE_NAME: str
    SCHEMA_FILE_PATH: str

    # ===============================
    # AWS Configuration
    # ===============================
    AWS_ACCESS_KEY_ID: SecretStr
    AWS_SECRET_ACCESS_KEY: SecretStr
    REGION_NAME: str
    MODEL_BUCKET_NAME: str
    MODEL_PUSHER_S3_KEY: str

    # ===============================
    # Data Ingestion
    # ===============================
    DATA_INGESTION_COLLECTION_NAME: str
    DATA_INGESTION_DIR_NAME: str
    DATA_INGESTION_FEATURE_STORE_DIR: str
    DATA_INGESTION_INGESTED_DIR: str
    DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float

    # ===============================
    # Data Validation
    # ===============================
    DATA_VALIDATION_DIR_NAME: str
    DATA_VALIDATION_REPORT_FILE_NAME: str

    # ===============================
    # Data Transformation
    # ===============================
    DATA_TRANSFORMATION_DIR_NAME: str
    DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str
    DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str

    # ===============================
    # Model Trainer
    # ===============================
    MODEL_TRAINER_DIR_NAME: str
    MODEL_TRAINER_TRAINED_MODEL_DIR: str
    MODEL_TRAINER_TRAINED_MODEL_NAME: str
    MODEL_TRAINER_EXPECTED_SCORE: float
    MODEL_TRAINER_MODEL_CONFIG_FILE_PATH: str
    MODEL_TRAINER_N_ESTIMATORS: int
    MODEL_TRAINER_MIN_SAMPLES_SPLIT: int
    MODEL_TRAINER_MIN_SAMPLES_LEAF: int
    MODEL_TRAINER_MAX_DEPTH: int
    MODEL_TRAINER_CRITERION: str
    MODEL_TRAINER_RANDOM_STATE: int

    # ===============================
    # Model Evaluation
    # ===============================
    MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE: float

    # ===============================
    # App Config
    # ===============================
    APP_HOST: str
    APP_PORT: int

    model_config = SettingsConfigDict(
        env_file=".env"
    )
CONFIG = Settings()
