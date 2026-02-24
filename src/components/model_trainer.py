import sys
import numpy as np
from typing import Tuple
from src.logger import logging
from src.exception import MyException
from src.entity.estimator import MyModel
from sklearn.tree import DecisionTreeClassifier
from src.entity.config_entity import ModelTrainerConfig
from sklearn.ensemble import RandomForestClassifier,VotingClassifier
from src.utils.main_utils import load_numpy_array_data, load_object, save_object
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from src.entity.artifact_entity import DataTransformationArtifact, ModelTrainerArtifact, ClassificationMetricArtifact

class ModelTrainer:
    def __init__(self, data_transformation_artifact: DataTransformationArtifact,
                 model_trainer_config: ModelTrainerConfig):
        """
        Discription: ModelTrainer Constructor.
        
        Args:
            data_transformation_artifact: Output reference of data transformation artifact stage
            model_trainer_config: Configuration for model training
        """
        self.data_transformation_artifact = data_transformation_artifact
        self.model_trainer_config = model_trainer_config


    def get_model_object_and_report(self, train: np.array, test: np.array) -> Tuple[object, object]:
        """
        Description:  This function trains a RandomForestClassifier with specified parameters
        
        Args: 
            train (np.array): Train data 
            test (np.array): Test data
        
        Outputs:
            Returns metric artifact object and trained model object
            
        Raises:
            Write an exception log and then raise an exception
        """
        try:
            logging.info("Training VotingClassifier with specified parameters")

            # Splitting the train and test data into features and target variables
            x_train, y_train, x_test, y_test = train[:, :-1], train[:, -1], test[:, :-1], test[:, -1]
            logging.info("train-test split done.")

            # Model Tranning: Initialize RandomForestClassifier with specified parameters
            
            dt = DecisionTreeClassifier(
                criterion=self.model_trainer_config._dt_criterion,
                max_depth=self.model_trainer_config._dt_max_depth,
                min_samples_leaf=self.model_trainer_config._dt_min_samples_leaf,
                min_samples_split=self.model_trainer_config._dt_min_sample_split
            )


            rf = RandomForestClassifier(
                criterion=self.model_trainer_config._rf_criterion,
                min_samples_split=self.model_trainer_config._rf_min_samples_split,
                n_estimators=self.model_trainer_config._rf_n_estimator 
            )

            model = VotingClassifier(estimators=[('rf',rf),('dt',dt)],voting="hard",flatten_transform=False,verbose=True)

            # Fit the model
            logging.info("Model training going on...")
            model.fit(x_train, y_train)
            logging.info("Model training done.")

            # Predictions and evaluation metrics
            y_pred = model.predict(x_test)
            accuracy = accuracy_score(y_test, y_pred)
            f1 = f1_score(y_test, y_pred)
            precision = precision_score(y_test, y_pred)
            recall = recall_score(y_test, y_pred)

            # Creating metric artifact
            metric_artifact = ClassificationMetricArtifact(f1_score=f1, precision_score=precision, recall_score=recall)
            return model, metric_artifact
        
        except Exception as e:
            raise MyException(e, sys) from e



    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")
        """
        Description: This function initiates the model training steps
        
        Output:
            Returns model trainer artifact
            
        Raises:
            Write an exception log and then raise an exception
        """
        try:
            print("----------------------------------------------------------------------------")
            print("Starting Model Trainer Component")
            # Load transformed train and test data
            train_arr = load_numpy_array_data(file_path=self.data_transformation_artifact.transformed_train_file_path)
            test_arr = load_numpy_array_data(file_path=self.data_transformation_artifact.transformed_test_file_path)
            logging.info("train-test data loaded")
            
            # Train model and get metrics
            trained_model, metric_artifact = self.get_model_object_and_report(train=train_arr, test=test_arr)
            logging.info("Model object and artifact loaded.")
            
            # Load preprocessing object
            preprocessing_obj = load_object(file_path=self.data_transformation_artifact.transformed_object_file_path)
            logging.info("Preprocessing obj loaded.")

            # Check if the model's accuracy meets the expected threshold
            if accuracy_score(train_arr[:, -1], trained_model.predict(train_arr[:, :-1])) < self.model_trainer_config.expected_accuracy:
                logging.info("No model found with score above the base score")
                raise Exception("No model found with score above the base score")

            # Save the final model object that includes both preprocessing and the trained model
            logging.info("Saving new model as performace is better than previous one.")
            my_model = MyModel(preprocessing_object=preprocessing_obj, trained_model_object=trained_model)
            save_object(self.model_trainer_config.trained_model_file_path, my_model)
            logging.info("Saved final model object that includes both preprocessing and the trained model")

            # Create and return the ModelTrainerArtifact
            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path=self.model_trainer_config.trained_model_file_path,
                metric_artifact=metric_artifact,
            )
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")
            return model_trainer_artifact
        
        except Exception as e:
            raise MyException(e, sys) from e
        