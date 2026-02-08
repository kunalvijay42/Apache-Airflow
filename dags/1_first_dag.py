from airflow.sdk import dag, task 

@dag(
        dag_id="first_dag",
)
def first_dag():

    @task.python    # Simlar to Python Operator, but more concise and easier to read
    def first_task():
        print("This is the first task")

    @task.python
    def second_task():
        print("This is the second task")
    
    @task.python
    def third_task():
        print("This is the third task. DAG complete!")
    
    
    # Defining task dependencies
    first = first_task()
    second = second_task()
    third = third_task()
    
    first >> second >> third   # Note - Always define the dependencies at the DAG level and not the task level.

# Instantiating/Registering the DAG
first_dag()