'''
This code defines a series of data containers using Python’s @dataclass decorator from the
 dataclasses module. These are used to structure and transport information cleanly between different stages 
 of a machine learning pipeline.

'''




from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:  # #Used to store paths to datasets split during ingestion:    
    trained_file_path:str 
    test_file_path:str

'''
   
#Captures the results of data validation
@dataclass
class DataValidationArtifact:
    validation_status:bool  ## Was validation successful?
    message: str                # Summary or error message
    validation_report_file_path: str     # File path to validation report


#Holds paths after data transformation (e.g., encoding, scaling):
@dataclass
class DataTransformationArtifact:
    transformed_object_file_path:str  # Path to saved transformer (e.g., pickle) 
    transformed_train_file_path:str   # Path to transformed training data
    transformed_test_file_path:str    # Path to transformed test data


#Stores evaluation metrics from model performance:
@dataclass
class ClassificationMetricArtifact:
    f1_score:float
    precision_score:float
    recall_score:float


#Represents output of model training
@dataclass
class ModelTrainerArtifact:
    trained_model_file_path:str   # Path to saved model
    metric_artifact:ClassificationMetricArtifact  #  # Embedded evaluation metrics

@dataclass
class ModelEvaluationArtifact:
    is_model_accepted:bool
    changed_accuracy:float
    s3_model_path:str 
    trained_model_path:str

@dataclass
class ModelPusherArtifact:
    bucket_name:str
    s3_model_path:str





     ┌──────────────────────────────┐
 │      Data Ingestion          │
 │                              │
 │ Reads raw data → splits →    │
 │ saves train/test files       │
 └────────────┬────────────────┘
              │
              ▼
┌──────────────────────────────┐
│   DataIngestionArtifact      │
│ ─ trained_file_path          │
│ ─ test_file_path             │
└────────────┬────────────────┘
              │
              ▼
 ┌──────────────────────────────┐
 │      Data Validation         │
 │                              │
 │ Validates schema, types,     │
 │ missing values etc.          │
 └────────────┬────────────────┘
              │
              ▼
┌──────────────────────────────┐
│   DataValidationArtifact     │
│ ─ validation_status          │
│ ─ message                    │
│ ─ validation_report_file_path│
└────────────┬────────────────┘
              │
              ▼
 ┌──────────────────────────────┐
 │   Data Transformation        │
 │                              │
 │ Scaling, encoding, saving    │
 │ transformed data + objects   │
 └────────────┬────────────────┘
              │
              ▼
┌──────────────────────────────┐
│ DataTransformationArtifact   │
│ ─ transformed_object_file_path│
│ ─ transformed_train_file_path │
│ ─ transformed_test_file_path  │
└────────────┬─────────────────┘
              │
              ▼
 ┌──────────────────────────────┐
 │       Model Training         │
 │                              │
 │ Train ML model, get metrics  │
 └────────────┬────────────────┘
              │
              ▼
┌──────────────────────────────┐
│ ClassificationMetricArtifact │
│ ─ f1_score                   │
│ ─ precision_score            │
│ ─ recall_score               │
└────────────┬────────────────┘
              │
              ▼
┌──────────────────────────────┐
│     ModelTrainerArtifact     │
│ ─ trained_model_file_path    │
│ ─ metric_artifact            │
└────────────┬────────────────┘
              │
              ▼
 ┌──────────────────────────────┐
 │     Model Evaluation         │
 │                              │
 │ Compares with old model      │
 └────────────┬────────────────┘
              │
              ▼
┌──────────────────────────────┐
│   ModelEvaluationArtifact    │
│ ─ is_model_accepted          │
│ ─ changed_accuracy           │
│ ─ s3_model_path              │
│ ─ trained_model_path         │
└────────────┬────────────────┘
              │
              ▼
 ┌──────────────────────────────┐
 │       Model Pusher           │
 │                              │
 │ Upload model to S3 / GCS     │
 └────────────┬────────────────┘
              │
              ▼
┌──────────────────────────────┐
│     ModelPusherArtifact      │
│ ─ bucket_name                │
│ ─ s3_model_path              │
└──────────────────────────────┘

    '''