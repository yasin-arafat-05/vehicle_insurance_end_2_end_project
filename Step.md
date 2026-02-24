### 1. Create the whole file structure:

```python
python template.py
```

### 2. Step- 2 
`Find the setup.py file  do necessary changes and  pyproject.toml file and make venv and  download all package. In requirements.txt add "-e ." it will convert all the local packages like external module for example fastapi,numpy,pandas etc. It will look like below:`

```cmd
pip list
src   0.0.1  /home/yasin/all_program/vehicle_insurance_end_2_end_project
```
### 3. Step-3 
`Write the logger file code logic into src/logger/__init__.py then test the logger from demo.py file`

### 4. Step-4
`Write the exception file code logic into src/exception/__init__.py  then test the exception from demo.py`


### 5. Step-5
`Create Nootbook, and do some expriment.`

### 6. Step-6: Data Ingestion
- 1. Declare variables within constants.__init__.py file and value from (.env)
- 2. add code to configuration.mongo_db_connections.py file and define the func for mondodb connection 
- 3. Inside "data_access" folder, add code to proj1_data that will use mongo_db_connections.py to connect with DB, fetch data in key-val format and transform that to df.
- 4. add code to entity.config_entity.py file till DataIngestionConfig class 
- 5. add code to entity.artifact_entity.py file till DataIngestionArtifact class 
- 6. add code to components.data_ingestion.py file 
- 7. add code to training pipeline 
- 8. run demo.py (set mongodb connection url first, see next step)



### 7. Data Validation, Data Transformation & Model Trainer:

- 1. Complete the work on utils.main_utils.py and config.schema.yaml file `(add entire info about dataset for data validation step)`
- 2. Now work on the "Data Validation" component the way we did in step 17 for Data Ingestion. (Workflow mentioned below)
- 3. Now work on the "Data Transformation" component the way we did in above step. (add estimator.py to entity folder)
- 4. Now work on the "Model Trainer" component the way we did in above step. (add class to estimator.py in entity folder)

- 5. Before moving to next component of Model Evaluation, some AWS services setup is needed:
      * Login to AWS console.
      * Keep region set as - us-east-1
      * Go to IAM >> Create new user (name: firstproj)
      * Attach policy >> select AdministratorAccess >> next >> create user
      * Go to the user >> Security Credentials >> Access Keys >> Create access key
      * Select CLI >> agree to condition >> next >> Create Access Key >> download csv file
      * Set env variables with above csv values using below method:
      * Now add the access key, secret key, region name to constants.__init__.py
      * Add code to src.configuration.aws_connection.py file (To work with AWS S3 service)
      * Ensure below info in constants.__init__.py file:
            MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE: float = 0.02
            MODEL_BUCKET_NAME = "my-model-mlopsproj"
            MODEL_PUSHER_S3_KEY = "model-registry"
      * Go to S3 service >> Create bucket >> Region: us-east-1 >> General purpose >>
        Bucket Name: "my-model-mlopsproj" >> uncheck: "Block all public access" and acknowledge >>
        Hit Create Bucket
      * Now inside "src.aws_storage" code needs to be added for the configurations needed to pull 
        and push model from AWS S3 bucket. 
      * Inside "entity" dir we will have an "s3_estimator.py" file containing all the func to pull/push
        data from s3 bucket.
        