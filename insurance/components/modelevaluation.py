from insurance.entity import artifact_entity,config_entity
from insurance.exception import InsuranceException
from insurance.logger import logging
from typing import Optional
import os,sys 
import xgboost as xg
from sklearn.linear_model import LinearRegression
from insurance import utils
from sklearn.metrics import r2_score
from insurance.predictor import ModelResolver

class ModelEvaluation:
    def __init__(self,model_eval_config: config_entity.ModelEvaluationConfig,
                        data_ingestion_artifact: artifact_entity.DataIngestionArtifact,
                        data_transformation_artifact: artifact_entity.DataTransformationArtifact,
                        model_trainer_artifact: artifact_entity.ModelTrainerArtifact):

        try:
            self.model_eval_config: model_eval_config
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_transformation_artifact = data_transformation_artifact
            self.model_trainer_artifact = model_trainer_artifact
            self.model_resolver = ModelResolver()
        except Exception as e:
            raise InsuranceException(e,sys)

    def initiate_model_evaluation(self)->artifact_entity.ModelEvaluationArtifact:
        try:
            #if saved model folder has model the we will compare 
            #which model is best trained or the model from saved model folder
            logging.info("if saved model folder has model the we will compare "
            "which model is best trained or the model from saved model folder")
            latest_dir_path = self.model_resolver.get_latest_dir_path()
            if latest_dir_path==None:
                model_eval_artifact = artifact_entity.ModelEvaluationArtifact(is_model_accepted=True,
                improved_accuracy=None)
                logging.info(f"Model evaluation artifact: {model_eval_artifact}")
                return model_eval_artifact
        except Exception as e:
            raise InsuranceException(e,sys)
