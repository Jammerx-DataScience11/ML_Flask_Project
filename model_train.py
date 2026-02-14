import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# simple tranining data 
x = [[1] , [2] , [3] , [4] , [5]]
y = [2 , 4 , 6 , 8 ,  10]

# create a model
model = LinearRegression()
model.fit(x,y)

pickle.dump(model, open('model.pkl' , 'wb'))


print("Model trained and saved successfully")




