# -*- coding: utf-8 -*-
# The challenge: build a model on RandomForestClassifier from data pipeline using scikit
# This is part 1 where the data is schema'd packaged by rf criteria
# and split for destination folder assignment

#import libraries
import os
import dataiku
import pandas as pd
import numpy as np
from sklearn.externals import joblib
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction import DictVectorizer
from sklearn.grid_search import GridSearchCV
from sklearn.ensemble import RandomForestClassifier


# Recipe inputs
df = dataiku.Dataset("train").get_dataframe()

# Settings
SCHEMA = {
          'target':'Churn',
          'features_num': [
                           'Account_Length', 'VMail_Message','Day_Mins', 'Day_Calls', 'Day_Charge', 'Eve_Mins',
          'Eve_Calls', 'Eve_Charge', 'Night_Mins', 'Night_Calls', 'Night_Charge', 'Intl_Mins',
          'Intl_Calls', 'Intl_Charge', 'CustServ_Calls'
                ],
          'features_cat': [
                           'State','Area_Code','Intl_Plan','VMail_Plan'
                ]
    }

# Preprocessing

# Numeric variables
df_num = df[SCHEMA['features_num']]
trf_num = Pipeline ([
                     ('imp', Imputer(strategy='median')),
                     ('sts', StandardScaler()),
                     ])
x_num = trf_num.fit_transform(df_num)

# Catagorical variables
df_cat = df[SCHEMA['features_cat']]
features = df_cat.columns

for feature in features:
    if df_cat[feature].dtype != 'object':
        df_cat[feature] = df_cat[feature].astype(str)

data = df_cat.to_dict(orient='records')

trf_cat = DictVectorizer(sparse=False)
x_cat = trf_cat.fit_transform(data)

# Concat of numeric and catagorical variables
X = np.concatenate((x_cat, x_num), axis=1)
Y = df[SCHEMA['target']].values

# Training of Model
param_grid = {
      'max_depth' : [3, None],
      'max_features' : [1, 3, 10],
      'min_samples_split' : [1, 3, 10],
      'min_samples_leaf' : [1, 3, 10],
      'bootstrap' : [True, False],
      'criterion' : ['gini', 'entropy']
}

clf = RandomForestClassifier()
gs = GridSearchCV(clf, param_grid=param_grid, n_jobs=-1, scoring='roc_auc')
gs.fit(X, Y)

# Recipe outputs
model_skikit = dataiku.Folder("70DO2Zpk").get_path() #Destination Folder

for file in os.listdir(model_skikit):
    try: os.remove_file()
    except: pass

serials = [
           {'pkl': 'schema.pkl','obj': SCHEMA},
           {'pkl': 'trf_num.pkl', 'obj': trf_num},
           {'pkl': 'trf_cat.pkl','obj': trf_cat},
           {'pkl': 'model.pkl','obj': gs.best_estimator_},
           ]

for serial in serials:
    fp = os.path.join(model_skikit, serial['pkl'])
    joblib.dump(serial['obj'], fp)
