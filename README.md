# Airflow and MLflow Integration Example

## Description
This project provides a comprehensive example of integrating Apache Airflow with MLflow. The collaboration between these two powerful tools facilitates the orchestration and tracking of machine learning workflows. The repository contains sample code showcasing how to set up DAGs (Directed Acyclic Graphs) in Airflow to schedule and manage MLflow experiments seamlessly.

## Key Features
- **DAG Configuration:** Demonstrates how to configure Airflow DAGs to orchestrate MLflow experiments.
- **MLflow Tracking:** Illustrates the integration of MLflow for experiment tracking and artifact logging.
- **Workflow Automation:** Shows how to automate end-to-end machine learning workflows using Airflow.
- **README.md Usage:**
  - **README.md Usage:**
  - Clone the repository.
    ```bash
    git clone https://github.com/v-onuphrienko/MLOPS3.3.git
    ```
  - Create and activate a virtual environment (venv):
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```
  - Install project dependencies:
    ```bash
    pip install -r requirements.txt
    ```
  - Review the example DAG in `dags/`.
  - Configure MLflow settings in `mlflow_config.yaml`.
  - Install dependencies with `pip install -r requirements.txt`.
  - Run Airflow webserver and scheduler: `airflow webserver -p 8080 &` and `airflow scheduler &`.
  - Run MLFlow webserver: `mlflow server --backend-store-uri postgresql://mlflow:mlflow@localhost/mlflow --default-artifact-root file:/home/‹user›/mlruns -h 0.0.0.0 -p 5000`.
  - Access the Airflow UI to view and trigger the DAG.

Feel free to customize and expand upon this example for your specific use cases. For detailed instructions, refer to the provided documentation within the repository.
