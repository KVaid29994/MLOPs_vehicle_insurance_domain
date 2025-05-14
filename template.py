'''
This script is used to automatically scaffold a full machine learning project structure. It:

Defines all folders and files required (mainly under a root src/ directory).

Automatically creates any missing directories and empty files.

Skips files that already exist and have content (to avoid overwriting).

Useful for bootstrapping standard pipelines (like ingestion, validation, transformation, etc.) with ready-to-edit modules.
'''


import os
from pathlib import Path

# Define the root folder name for the project

project_name = "src"

# List of all files (with paths) that need to be created as part of the project structure

list_of_files = [

    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",  
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/mongo_db_connection.py",
    f"{project_name}/configuration/aws_connection.py",
    f"{project_name}/cloud_storage/__init__.py",
    f"{project_name}/cloud_storage/aws_storage.py",
    f"{project_name}/data_access/__init__.py",
    f"{project_name}/data_access/proj1_data.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/estimator.py",
    f"{project_name}/entity/s3_estimator.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipline/__init__.py",
    f"{project_name}/pipline/training_pipeline.py",
    f"{project_name}/pipline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "pyproject.toml",
    "config/model.yaml",
    "config/schema.yaml",
]

# Loop through each file path in the list

for filepath in list_of_files: 
    filepath = Path(filepath)  # Convert string path to a platform-independent Path object
    filedir, filename = os.path.split(filepath) # Split path into directory and file name

    # If the directory part is not empty, create the directory (if it doesn't exist)

    if filedir != "": 
        os.makedirs(filedir, exist_ok=True)

     # Create the file only if it doesn't exist or if it's an empty file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
     # If file already exists and is non-empty, log its presence
    else:
        print(f"file is already present at: {filepath}")