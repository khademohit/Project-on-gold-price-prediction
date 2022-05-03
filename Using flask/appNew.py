from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("Prediction.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    
    end=int(request.form.values())
    print(end)
    prediction=model.predict(2183,end)
    output=prediction



if __name__ == '__main__':
    app.run(debug=True)