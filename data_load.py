import numpy as np 
import pandas as pd
from pymongo import MongoClient
import json

episodeIV = pd.read_csv('./SW_EpisodeIV.txt', delim_whitespace=True, names=["index","character","dialogue"] ,header = None)
episodeV = pd.read_csv('./SW_EpisodeV.txt', delim_whitespace=True, names=["index","character","dialogue"] ,header = None)
episodeVI = pd.read_csv('./SW_EpisodeVI.txt', delim_whitespace=True, names=["index","character","dialogue"] ,header = None)


client = MongoClient()
db = client['star_wars']
movies = db['movies']

recordsIV = json.loads(episodeIV.T.to_json()).values()
movies.insert_many(recordsIV)
recordsV = json.loads(episodeV.T.to_json()).values()
movies.insert_many(recordsV)
recordsVI = json.loads(episodeVI.T.to_json()).values()
movies.insert_many(recordsVI)
print(str(movies.count_documents({}))+' entries inserted!')