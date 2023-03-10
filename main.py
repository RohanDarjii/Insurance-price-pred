import os, sys
from insurance.components.datavalidation import DataValidation
from insurance.components.modelevaluation import ModelEvaluation
from insurance.components.modelpusher import ModelPusher
from insurance.components.modeltrainer import ModelTrainer
from insurance.logger import logging
from insurance.exception import InsuranceException
from insurance.utils import get_collection_as_dataframe
from insurance.entity.config_entity import DataIngestionConfig, TraningPipelineConfig
from insurance.entity import config_entity
from insurance.components.dataIngestion import DataIngestion
from insurance.components.datatransformation import DataTransformation



if __name__ == "__main__":
    try:
        #get_collection_as_dataframe(database_name="insurance", collection_name="insurance_data")
        training_pipeline_config = config_entity.TraningPipelineConfig()
        data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config= training_pipeline_config)
        print(data_ingestion_config.to_dict())
        data_ingestion = DataIngestion(data_ingestion_config= data_ingestion_config)
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        #data_validation
        data_validation_config = config_entity.DataValidationConfig(training_pipeline_config= training_pipeline_config)
        data_validation = DataValidation(data_validation_config= data_validation_config, data_ingestion_artifact= data_ingestion_artifact)
        data_validation_artifact = data_validation.initiate_data_validation()
        #Data Transformation
        data_transformation_config = config_entity.DataTransformationConfig(training_pipeline_config= training_pipeline_config)
        data_transformation = DataTransformation(data_transformation_config=data_transformation_config, 
        data_ingestion_artifact=data_ingestion_artifact)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        #model trainer
        model_trainer_config = config_entity.ModelTrainerConfig(training_pipeline_config= training_pipeline_config)
        model_trainer = ModelTrainer(model_trainer_config=model_trainer_config, data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact = model_trainer.initiate_model_trainer()
        #model evaluation
        model_eval_config = config_entity.ModelEvaluationConfig(training_pipeline_config= training_pipeline_config)
        model_eval  = ModelEvaluation(model_eval_config=model_eval_config,
        data_ingestion_artifact=data_ingestion_artifact,
        data_transformation_artifact=data_transformation_artifact,
        model_trainer_artifact=model_trainer_artifact)
        model_eval_artifact = model_eval.initiate_model_evaluation()
        # model pusher
        model_pusher_config = config_entity.ModelPusherConfig(training_pipeline_config= training_pipeline_config)
        model_pusher = ModelPusher(model_pusher_config=model_pusher_config,
                                        data_transformation_artifact=data_transformation_artifact,
                                        model_trainer_artifact=model_trainer_artifact)
        model_pusher_artifact = model_pusher.initiate_model_pusher()
    except Exception as e:
          print(e)

