
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
import papermill as pm

# Define default arguments
default_args = {
   'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'email_on_success': True,  # Enable email on success
    'email': ['shrinivas.bhusannavar@sjsu.edu'],  # Replace with your email address
}

# Define function to run a notebook with Papermill
def run_notebook(notebook_path, output_path):
    pm.execute_notebook(
        notebook_path,
        output_path,
    )

# Initialize the DAG
with DAG(
    'run_notebooks',
    default_args=default_args,
    description='DAG to run BigQuery notebooks in sequence with Papermill',
    schedule_interval=None,
    start_date=days_ago(1),
    catchup=False,
) as dag:

    # Preprocessing Tasks
    preprocess_iqlinic = PythonOperator(
        task_id='preprocess_iqlinic',
        python_callable=run_notebook,
        op_args=[
            "gs://notebooksz/iqlinic_preprocessing.ipynb",
            "/tmp/output_iqlinic_preprocessing.ipynb"
        ]
    )

    preprocess_healthcaremagic = PythonOperator(
        task_id='preprocess_healthcaremagic',
        python_callable=run_notebook,
        op_args=[
            "gs://notebooksz/healthcaremagic_preprocessing.ipynb",
            "/tmp/output_healthcaremagic_preprocessing.ipynb"
        ]
    )

    preprocess_mimic = PythonOperator(
        task_id='preprocess_mimic',
        python_callable=run_notebook,
        op_args=[
            "gs://notebooksz/mimic_preprocessing.ipynb",
            "/tmp/output_mimic_preprocessing.ipynb"
        ]
    )

    # Transformation Tasks
    run_iqlinic = PythonOperator(
        task_id='run_iqlinic_transformation',
        python_callable=run_notebook,
        op_args=[
            "gs://notebooksz/iqlinic_transformation.ipynb",
            "/tmp/output_iqlinic.ipynb"
        ]
    )

    run_healthcaremagic = PythonOperator(
        task_id='run_healthcaremagic_transformation',
        python_callable=run_notebook,
        op_args=[
            "gs://notebooksz/healthcaremagic_transformation.ipynb",
            "/tmp/output_healthcaremagic.ipynb"
        ]
    )

    run_mimic = PythonOperator(
        task_id='run_mimic_transformation',
        python_callable=run_notebook,
        op_args=[
            "gs://notebooksz/mimic_transformation.ipynb",
            "/tmp/output_mimic.ipynb"
        ]
    )

    # Final Data Preparation Task
    data_preparation = PythonOperator(
        task_id='data_preparation',
        python_callable=run_notebook,
        op_args=[
            "gs://notebooksz/final_data_preparation.ipynb",
            "/tmp/output_data_preparation.ipynb"
        ]
    )

    # Define task order
    preprocess_iqlinic >> run_iqlinic
    preprocess_healthcaremagic >> run_healthcaremagic
    preprocess_mimic >> run_mimic
    run_iqlinic >> run_healthcaremagic >> run_mimic >> data_preparation
