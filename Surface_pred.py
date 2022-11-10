# Importing the required libraries.
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
import matplotlib.pyplot as plt

# Reading the dataset and checking the data.
df=pd.read_csv('data.csv')
df.head()

# Assigning independent and dependent varibles.
X=df[['layer_height']]
y=df[['roughness']]

# Splitting the data into traning and testing (80-20 split).
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=4)

# Importing the Linear Regression Module.
from sklearn.linear_model import LinearRegression
model =LinearRegression()

#Fitting the model to the training data.
model.fit(X_train,y_train)

# Predicting the values for X_test after training the model.
predicted_values=model.predict(X_test)

# Evaluating the perfromance of the model with R2 Score.
print('The r2_score of the Linear Regression model is:',r2_score(y_test,predicted_values))

#The r2 score observed is 0.785 or the model explains about 78.5% of the 
# variance. Hence, a good model as r2 score or R-squared always lies between 0 
# and1.

# Feature extraction.
df.replace(['grid','honeycomb','abs','pla'],[1,0,1,0],inplace=True)

# Dropping columns that aren't required.
qw=df.drop(['tension_strenght','elongation'],axis=1)

# Identifying the features.
# Dropping the dependent variable from the independent data and assigning it to 
# the dependent variable
X1=qw.drop(['roughness'],axis=1)
y1=qw['roughness']

# Fitting the model to Random Forest Regressor to identify the important features.
rf=RandomForestRegressor()
rf.fit(X1,y1)
fi=rf.feature_importances_

#Plotting the features importances.
plt.figure(figsize=(9,7))
plt.bar(X1.columns,fi)
plt.xticks(rotation=90)
plt.show()

# From the above graph, it is evident that the features, layer_height,
# nozzle_temperature, print_speed, infill_density, wall_thickness are the 
# most influencing parameters.

#Building the gradient boosting regressor model.
# Choosing the influencing params from the above feature importance 
X2=qw[['layer_height','nozzle_temperature','print_speed','infill_density','wall_thickness']]
y2=qw[['roughness']]

#Splitting the data into training and testing samples in the ratio of 80:20
from sklearn.model_selection import train_test_split
X2_train,X2_test,y2_train,y2_test=train_test_split(X2,y2,test_size=0.2,random_state=4)

#Importing the required model.
model1=GradientBoostingRegressor()
model1.fit(X2_train,y2_train)

# Predicting the values for X_test after training the model.
predicted_values_gradboost_reg=model.predict(X2_test)

# Evaluating the performance of the model.
print('The r2_score of the Gradient Boosting Regression model is:',r2_score(y2_test,predicted_values_gradboost_reg))

#From the above observation, the model performed better than the Linear 
# Regression Model with an r2 score of 0.964 or the model explains 96.4% of 
# the variance in the data.
