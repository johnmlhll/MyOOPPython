# -*- coding: utf-8 -*-
#The Challenge: Part 2 of 2: Create a predictive model using RandomForestClassifiers and scikit

#Import Libraries
import os
import dataiku
import pandas as pd
import numpy as np
import sklearn as sk
from sklearn.externals import joblib

# Recipe Inputs
folder_path = dataiku.Folder("70DO2Zpk").get_path()
df = dataiku.Dataset("test").get_dataframe()

# Scikit Objects
schema = joblib.load(os.path.join(folder_path, 'schema.pkl'))
trf_num = joblib.load(os.path.join(folder_path, 'trf_num.pkl'))
trf_cat = joblib.load(os.path.join(folder_path, 'trf_cat.pkl'))
clf = joblib.load(os.path.join(folder_path, 'model.pkl'))


# Transform and Score the dataset
# Preprocess numerical features
x_num = trf_num.transform(df[schema['features_num']])

# Preprocess catagorical features
df_cat = df[schema['features_cat']]
features = df_cat.columns

for feature in features:
    if df_cat[feature].dtype != 'object':
        df_cat[feature] = df_cat[feature].astype(str)
data = df_cat.to_dict(orient = 'records')

x_cat = trf_cat.transform(data)


# Concatenate data
X = np.concatenate((x_cat, x_num), axis = 1)

# Score the new records
scores = clf.predict_proba(X)

# Reshape the model back to to the source dataset
preds = pd.DataFrame(scores, index = df.index).rename(columns = {0: 'proba_false', 1: 'proba_true'})
all_preds = df.join(preds)

# Receipe Output
test_scored_scikit = dataiku.Dataset("test_scored_scikit")
test_scored_scikit.write_with_schema(all_preds)
