import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model
import joblib

data=pd.read_csv("C:/Users/Dell/Desktop/BA project/christ college atm.csv")

features=data.copy()

features['Weekday Id']=data['Weekday'].astype("category").cat.codes
days={"Sunday":0,"Monday":1,"Tuesday":2,"Wednesday":3,"Thursday":4,"Friday":5,"Saturday":6,"SUNDAY":0,"MONDAY":1,"TUESDAY":2,"WEDNESDAY":3,"THURSDAY":4,"FRIDAY":5,"SATURDAY":6}
for i in range(data.shape[0]):
    features.loc[i,"Weekday Id"]=days[data.loc[i,"Weekday"]]
features['Festival Religion Id']=data['Festival Religion'].astype("category").cat.codes
features['Working Day Id']=data['Working Day'].astype("category").cat.codes
features['Holiday Sequence Id']=data['Holiday Sequence'].astype("category").cat.codes

x= features[["No Of Withdrawals","Weekday Id","Festival Religion Id","Working Day Id","Holiday Sequence Id"]]
y= features['Total amount Withdrawn'].copy()
x_train, x_test, y_train, y_test = train_test_split(x, y, shuffle= False, test_size = 0.2, random_state = 42)

model=linear_model.LinearRegression()
model.fit(x_train,y_train)
linpred=model.predict(x_test).round(decimals=0)


joblib.dump(model,"linear_Regression.pkl")

