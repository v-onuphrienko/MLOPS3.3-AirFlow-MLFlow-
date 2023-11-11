import requests
import json
from pyyoutube import Api
import os
 
import mlflow
from mlflow.tracking import MlflowClient
 
os.environ["MLFLOW_REGISTRY_URI"] = "/home/vlad/project/mlflow/"
mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("get_data")
 
key = "#Your API_KEY"
api = Api(api_key=key)
query = "'Mission Impossible'"
video = api.search_by_keywords(q=query, search_type=["video"], count=10, limit=30)
maxResults = 100
nextPageToken = ""
s = 0
 
with mlflow.start_run():
    for i, id_ in enumerate([x.id.videoId for x in video.items]):
        uri = "https://www.googleapis.com/youtube/v3/commentThreads?" + \
              "key={}&textFormat=plainText&" + \
              "part=snippet&" + \
              "videoId={}&" + \
              "maxResults={}&" + \
              "pageToken={}"
        uri = uri.format(key, id_, maxResults, nextPageToken)
        content = requests.get(uri).text
        data = json.loads(content)
        for item in data['items']:
            s += int(item['snippet']['topLevelComment']['snippet']['likeCount'])
    mlflow.log_artifact(local_path="/home/vlad/project/scripts/get_data.py",
                        artifact_path="get_data code")
    mlflow.end_run()
 
with open('/home/vlad/project/datasets/data.csv', 'a') as f:
    f.write("{}\n".format(s))