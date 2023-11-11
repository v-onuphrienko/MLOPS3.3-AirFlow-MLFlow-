from sklearn.linear_model import LinearRegression
import pickle
import pandas as pd
import os
 
import mlflow
from mlflow.tracking import MlflowClient
 
mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("train_model")
 
df = pd.read_csv('/home/vlad/project/datasets/data_train.csv', header=None)
df.columns = ['id', 'counts']
model = LinearRegression()
 
with mlflow.start_run():
    mlflow.sklearn.log_model(model,
                             artifact_path="lr",
                             registered_model_name="lr")
    mlflow.log_artifact(local_path="/home/vlad/project/scripts/train_model.py",
                        artifact_path="train_model code")
    mlflow.end_run()
 
model.fit(df['id'].values.reshape(-1,1), df['counts'])
 
with open('/home/vlad/project/models/data.pickle', 'wb') as f:
    pickle.dump(model, f)