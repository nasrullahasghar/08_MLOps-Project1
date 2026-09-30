"""
Project Structure Generator
Creates a modular ML project directory layout.
"""

from pathlib import Path

PROJECT_NAME = "src"

LIST_OF_FILES = [
    # Package init
    f"{PROJECT_NAME}/__init__.py",
    
    # ML Pipeline Components
    f"{PROJECT_NAME}/components/__init__.py",
    f"{PROJECT_NAME}/components/data_ingestion.py",
    f"{PROJECT_NAME}/components/data_validation.py",
    f"{PROJECT_NAME}/components/data_transformation.py",
    f"{PROJECT_NAME}/components/model_trainer.py",
    f"{PROJECT_NAME}/components/model_evaluation.py",
    f"{PROJECT_NAME}/components/model_pusher.py",
    
    # Configuration
    f"{PROJECT_NAME}/configuration/__init__.py",
    f"{PROJECT_NAME}/configuration/mongo_db_connection.py",
    f"{PROJECT_NAME}/configuration/aws_connection.py",
    
    # Cloud Storage
    f"{PROJECT_NAME}/cloud_storage/__init__.py",
    f"{PROJECT_NAME}/cloud_storage/aws_storage.py",
    
    # Data Access Layer
    f"{PROJECT_NAME}/data_access/__init__.py",
    f"{PROJECT_NAME}/data_access/proj1_data.py",
    
    # Constants & Entities
    f"{PROJECT_NAME}/constants/__init__.py",
    f"{PROJECT_NAME}/entity/__init__.py",
    f"{PROJECT_NAME}/entity/config_entity.py",
    f"{PROJECT_NAME}/entity/artifact_entity.py",
    f"{PROJECT_NAME}/entity/estimator.py",
    f"{PROJECT_NAME}/entity/s3_estimator.py",
    
    # Exception & Logging
    f"{PROJECT_NAME}/exception/__init__.py",
    f"{PROJECT_NAME}/logger/__init__.py",
    
    # Pipelines  <-- fixed typo: pipline -> pipeline
    f"{PROJECT_NAME}/pipeline/__init__.py",
    f"{PROJECT_NAME}/pipeline/training_pipeline.py",
    f"{PROJECT_NAME}/pipeline/prediction_pipeline.py",
    
    # Utilities
    f"{PROJECT_NAME}/utils/__init__.py",
    f"{PROJECT_NAME}/utils/main_utils.py",
    
    # Root-level files
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "pyproject.toml",
    
    # Config files
    "config/model.yaml",
    "config/schema.yaml",
]


def create_project_structure(files: list[str], project_name: str) -> None:
    """Create directories and empty files for the project."""
    for filepath in files:
        path = Path(filepath)
        
        # Create parent directories if they don't exist
        if path.parent != Path("."):
            path.parent.mkdir(parents=True, exist_ok=True)
        
        # Create file only if it doesn't exist or is empty
        if not path.exists() or path.stat().st_size == 0:
            path.touch()
            print(f"Created: {path}")
        else:
            print(f"Already exists (skipped): {path}")


if __name__ == "__main__":
    create_project_structure(LIST_OF_FILES, PROJECT_NAME)
    print("\nProject structure created successfully.")