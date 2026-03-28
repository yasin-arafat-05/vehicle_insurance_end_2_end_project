
# 🚗 Vehicle Insurance Prediction Project

## 📌 Project Overview
The goal of this project is to build an end-to-end Machine Learning solution to predict whether a customer will be interested in **Vehicle Insurance**. By analyzing customer demographics (Age, Gender) and vehicle details (Vehicle Age, Damage history), the model helps insurance providers target the right audience.

---

## 🏗️ System Architecture
The project is structured into two main components: the **Data/Training Pipeline** and the **Web/Prediction Service**.

### 1. Data & Training Pipeline
* **Data Ingestion:** Fetches data dynamically from **MongoDB Atlas**.
* **Data Validation:** Checks data types and schemas to ensure "Garbage In, Garbage Out" doesn't happen.
* **Data Transformation:** Handles feature engineering (e.g., encoding "Vehicle Age").
* **Model Training & Evaluation:** Trains the classifier and compares performance against a "base" model.
* **Model Pusher:** Deploys the best-performing model to cloud storage (AWS S3) for production use.

### 2. Web Application (FastAPI)
The project uses **FastAPI** to serve the model to end-users via a web interface.
* **GET /train**: Triggers the entire modular pipeline.
* **POST /**: Predicts insurance interest based on form inputs.

---

## 📂 Modular Project Structure
Here is how the project is organized to ensure professional-grade code quality:

| Directory/File | Purpose |
| :--- | :--- |
| **`src/components/`** | The core ML steps: Ingestion, Validation, Transformation, and Training. |
| **`src/configuration/`** | Logic for connecting to MongoDB and AWS services. |
| **`src/data_access/`** | Specialized methods to interact with the database specifically for this dataset. |
| **`src/entity/`** | Defines **Config Entities** (inputs for components) and **Artifact Entities** (outputs like CSVs/Models). |
| **`src/pipeline/`** | Orchestrates the components. Connects the dots from raw data to a trained model. |
| **`src/utils/`** | Helper functions for common tasks like saving/loading pickles or YAML files. |
| **`config/`** | Contains `schema.yaml` to define expected columns and `model.yaml` for hyperparameters. |

---

## 🛠️ Tech Stack
* **Language:** Python 3.11.9
* **Framework:** FastAPI
* **Database:** MongoDB Atlas
* **Cloud Storage:** AWS S3
* **Containerization:** Docker
* **Libraries:** Scikit-learn, imblearn, Pandas, Pymongo

---

## 🚀 How to Run
1. **Clone & Install:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Environment Setup:** Ensure your MongoDB URI and AWS credentials are set.
3. **Run the App:**
   ```bash
   python app.py
   ```
4. **Train & Predict:** - Visit `http://localhost:8080/train` to train.
   - Use the home page to test predictions.

