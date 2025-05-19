import os
from src.constants import *
from dataclasses import dataclass
from datetime import datetime

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

@dataclass
class TrainingPipelineConfig:
    pipeline_name: str = PIPELINE_NAME
    artifact_dir: str = os.path.join(ARTIFACT_DIR, TIMESTAMP)
    timestamp: str = TIMESTAMP


training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig()

@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_INGESTION_DIR_NAME)
    feature_store_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR, FILE_NAME)
    training_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TRAIN_FILE_NAME)
    testing_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TEST_FILE_NAME)
    train_test_split_ratio: float = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
    collection_name:str = DATA_INGESTION_COLLECTION_NAME


@dataclass
class DataValidationConfig:
    data_validation_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_VALIDATION_DIR_NAME)
    validation_report_file_path: str = os.path.join(data_validation_dir, DATA_VALIDATION_REPORT_FILE_NAME)

@dataclass
class DataTransformationConfig:
    data_transformation_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_TRANSFORMATION_DIR_NAME)
    transformed_train_file_path: str = os.path.join(data_transformation_dir, DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
                                                    TRAIN_FILE_NAME.replace("csv", "npy"))
    transformed_test_file_path: str = os.path.join(data_transformation_dir, DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
                                                   TEST_FILE_NAME.replace("csv", "npy"))
    transformed_object_file_path: str = os.path.join(data_transformation_dir,
                                                     DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR,
                                                     PREPROCESSING_OBJECT_FILE_NAME)
    
@dataclass
class ModelTrainerConfig:
    model_trainer_dir: str = os.path.join(training_pipeline_config.artifact_dir, MODEL_TRAINER_DIR_NAME)
    trained_model_file_path: str = os.path.join(model_trainer_dir, MODEL_TRAINER_TRAINED_MODEL_DIR, MODEL_FILE_NAME)
    expected_accuracy: float = MODEL_TRAINER_EXPECTED_SCORE
    model_config_file_path: str = MODEL_TRAINER_MODEL_CONFIG_FILE_PATH
    _n_estimators = MODEL_TRAINER_N_ESTIMATORS
    _min_samples_split = MODEL_TRAINER_MIN_SAMPLES_SPLIT
    _min_samples_leaf = MODEL_TRAINER_MIN_SAMPLES_LEAF
    _max_depth = MIN_SAMPLES_SPLIT_MAX_DEPTH
    _criterion = MIN_SAMPLES_SPLIT_CRITERION
    _random_state = MIN_SAMPLES_SPLIT_RANDOM_STATE

@dataclass
class ModelEvaluationConfig:
    changed_threshold_score: float = MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE
    bucket_name: str = MODEL_BUCKET_NAME
    s3_model_key_path: str = MODEL_FILE_NAME

@dataclass
class ModelPusherConfig:
    bucket_name: str = MODEL_BUCKET_NAME
    s3_model_key_path: str = MODEL_FILE_NAME

# @dataclass
# class VehiclePredictorConfig:
#     model_file_path: str = MODEL_FILE_NAME
#     model_bucket_name: str = MODEL_BUCKET_NAME


'''
🎯 Why You Need This File
It defines structured configuration classes for each pipeline stage using @dataclass, helping you:

✅ 1. Centralize Pipeline Configurations
Instead of hardcoding values throughout your project (which is error-prone and hard to maintain), this central file pulls constants from src.constants and structures them into meaningful classes.

✅ 2. Time-Based Artifacts
python
Copy
Edit
TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
You’re generating a unique folder for each run (using timestamp) so that:

Each pipeline run is tracked independently.

You avoid overwriting old models, logs, or datasets.

✅ 3. Organize Stage-Wise Outputs
Each config class defines directory structure and paths for artifacts:

DataIngestionConfig – controls where raw, train, and test files are stored.

DataValidationConfig – where the validation report is saved.

DataTransformationConfig – paths to transformed .npy files and preprocessors.

ModelTrainerConfig – contains hyperparameters + model path.

ModelEvaluationConfig – defines comparison threshold + S3 config.

ModelPusherConfig – S3 bucket upload paths.

VehiclePredictorConfig – used later in inference (loading model for predictions).

✅ 4. Parameter Injection to Code
This design allows you to pass configuration objects easily:

python
Copy
Edit
def start_data_ingestion(config: DataIngestionConfig):
    # use config.training_file_path, config.collection_name, etc.
Rather than hardcoding or reading from .yaml or .json everywhere, configs come preloaded via @dataclass.

✅ 5. Promotes Scalability and Maintainability
If your project expands:

Want to change directory layout? Just update constants.py.

New model version? Add to ModelTrainerConfig.

Migrate from local to S3? Update paths centrally.

'''