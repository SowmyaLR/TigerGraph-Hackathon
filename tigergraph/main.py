import pyTigerGraphBeta as tg
# import streamlit as st
import pandas as pd
import numpy as np
import datetime

TG_HOST = "url"
TG_USERNAME = "username"
TG_PASSWORD = "password"
TG_GRAPH = "graph_name"
TG_SECRET = "secret"

conn = tg.TigerGraphConnection(host=TG_HOST, graphname=TG_GRAPH, username=TG_USERNAME, password=TG_PASSWORD)
token = conn.getToken(TG_SECRET)
ls = conn.runInstalledQuery("Patientlist")
res = ls[0]["res"]
data_mp = []
for val in res:
  data_mp.append(val["attributes"])

patient_data = pd.DataFrame(list(data_mp))

patient_data["age"] = datetime.datetime.now().year - patient_data["birth_year"]
age_data = patient_data[patient_data["age"]!=datetime.datetime.now().year]

def get_columns():
  return list(patient_data.columns)


def get_infectious_data(field):
  infection_case_data = patient_data[field].value_counts().nlargest(n=10)
  infectious_col = infection_case_data.index.tolist()
  return np.reshape(np.array(infection_case_data.values.tolist()), (-1, len(infectious_col))), infectious_col

def get_unique_patient_attribute(field):
  return list(patient_data[field].unique())
