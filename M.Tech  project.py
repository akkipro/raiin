import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
from keras.models import load_model
from sklearn.preprocessing import StandardScaler
from sklearn import metrics

sc = StandardScaler()
app = Flask(__name__)



import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import pickle
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

import os
#print(os.listdir("../input"))


import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline



dataset = pd.read_csv('E:\dataset\weatherAUS.csv')

hk = dataset.head()
hi = hk
#hi = hk.to_string()
#hk = pd.DataFram(dataset)
dataset.drop(labels = ['Date','Location','Evaporation','Sunshine','Cloud3pm','Cloud9am','RISK_MM'],axis = 1,inplace = True)
dataset.drop(labels = ['WindGustDir','WindDir9am','WindDir3pm'],axis = 1,inplace = True)
da = dataset.head()
#daa = da.to_html()

na = dataset.isnull().sum()
naaa = na.reset_index()

dataset['RainToday'].replace({'No':0,'Yes':1},inplace = True)
dataset['RainTomorrow'].replace({'No':0,'Yes':1},inplace = True)

po = dataset.head()
poo = po

'''
for i in dataset:
    if dataset[i].isnull().sum()!=0:
        dataset[i].fillna(dataset[i].median(), inplace = True)

'''


dataset.fillna(dataset.median(), inplace=True)
naa = dataset.isnull().sum().reset_index()


from sklearn.preprocessing import StandardScaler
sc = StandardScaler()


x = dataset.drop(labels = ['RainTomorrow'],axis = 1)
xx= x.head(5)


y = dataset['RainTomorrow']
ya = dataset['RainTomorrow'].head(16)
yaa = ya.reset_index()


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 40)
x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.2, random_state=40)


import keras
from keras.models import Sequential,save_model
from keras.layers import Dense


classifier = Sequential()

classifier.add(Dense(units =30,kernel_initializer='uniform',activation = 'relu',input_dim = 13))
classifier.add(Dense(units = 30,kernel_initializer='uniform',activation = 'relu'))
classifier.add(Dense(units = 30,kernel_initializer='uniform',activation = 'relu'))
classifier.add(Dense(units = 1,activation='sigmoid',kernel_initializer='uniform'))


classifier.compile(optimizer = 'adam',loss = 'binary_crossentropy',metrics = ['accuracy'])

classifier.fit(x_train,y_train,epochs =15,batch_size=87,validation_data=(x_val, y_val))

y_pred = classifier.predict_classes(x_test)
y_train_pred = classifier.predict_classes(x_train)

from sklearn.metrics import accuracy_score

print('Training Accuracy ---->',accuracy_score(y_train,y_train_pred))
print('Testing Accuracy  ---->',accuracy_score(y_test,y_pred))



print("Precision:",metrics.precision_score(y_test, y_pred))

# Model Recall: what percentage of positive tuples are labelled as such?
print("Recall:",metrics.recall_score(y_test, y_pred))




@app.route('/')
def next1():
    return render_template('new.html', head = hi , gh = 'hello')
    
@app.route('/1')
def home():
    return render_template('1.html', head = da)

@app.route('/2')
def next2():
    return render_template('2.html', head = naaa)


@app.route('/3')
def next3():
    return render_template('3.html', head = poo)

@app.route('/4')
def next4():
    return render_template('4.html', head = naa)

@app.route('/5')
def next5():
    return render_template('5.html', head = yaa , x = xx)

@app.route('/55')
def next55():
    return render_template('55.html', head = yaa )
    
@app.route('/6')
def next6():
    return render_template('index.html')   

@app.route('/predict',methods=['POST'])
def predict():
   
    a= float(request.form['a'])
    b= float(request.form['b'])
    c= float(request.form['c'])
    d= float(request.form['d'])
    e= float(request.form['e'])
    f= float(request.form['f'])
    g= float(request.form['g'])
    h= float(request.form['h'])
    i= float(request.form['i'])
    j= float(request.form['j'])
    k= float(request.form['k'])
    l= float(request.form['l'])
    m= float(request.form['m'])
    
    m = pd.DataFrame({'a':a, 'b':b,'c': c,'d': d,'e': e, 'f':f, 'g':g, 'h':h, 'i':h,'j': j, 'k':k, 'l':l,'m': m}, index=[0])
    #m = pd.DataFrame({'a':a, 'b':b,'c': c,'d': d,'e': e, 'f':f, 'g':g, 'h':h, 'i':h,'j': j, 'k':k, 'l':l,'m': m}, index=[0])
   
    #km = pd.DataFrame({'a':9.7, 'b':31,'c': 0.0,'d': 80,'e': 7, 'f':28, 'g':42, 'h':9, 'i':1008.9,'j': 1003.6, 'k':18, 'l':30,'m':0.0}, index=[0])
   

    op = pd.DataFrame({'a':20.9, 'b':27.5,'c': 23.8,'d': 48.0,'e': 26.0, 'f':26.0, 'g':76.0, 'h':90.0, 'i':1012.1,'j': 1009.7, 'k':23.8, 'l':22.7,'m':1.0}, index=[0])
    
    prediction = classifier.predict_classes(m)
    pred = classifier.predict(m)
    
    return render_template('rain.html', prediction = prediction  , pred = pred)



if __name__ == "__main__":
    app.run(debug=True)