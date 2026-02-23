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

