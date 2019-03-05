import numpy as np
import pandas as pd
from sklearn.preprocessing import Imputer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import  GaussianNB
from sklearn.tree import DecisionTreeClassifier
def load_dataset(feature_paths,label_paths):
    feature=np.ndarray (shape= (0,41))
    label=np.ndarray (shape= (0,1))
    for file in feature_paths :
        df=pd.read_table (file,delimiter= ',',na_values= '?',header= None )
        imp=Imputer (missing_values= 'NaN',strategy= 'mean',axis= 0)
        imp.fit(df)
        df=imp.transform(df)
        feature =np.concatenate ((feature .df))