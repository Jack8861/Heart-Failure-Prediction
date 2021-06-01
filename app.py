""""
Created on Friday May 07 07-05-2021

@author: Syed Rahim Saqib
"""

from flask import Flask,request, render_template
from flask_cors import CORS,cross_origin
import joblib


app = Flask(__name__)

clusterer = joblib.load('models/clusterer')
RF_model1 = joblib.load('models/RF_model1')
RF_model2 = joblib.load('models/RF_model2')


@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict', methods=['GET','POST'])
def predict():

    age = int(request.form['age'])
    anaemia = int(request.form['anaemia'])
    creatinine_phosphokinase= int(request.form['creatinine_phosphokinase'])
    diabetes = int(request.form['diabetes'])
    ejection_fraction = int(request.form['ejection_fraction'])
    high_blood_pressure = int(request.form['high_blood_pressure'])
    platelets = float(request.form['platelets'])
    serum_creatinine = float(request.form['serum_creatinine'])
    serum_sodium = int(request.form['serum_sodium'])
    sex = int(request.form['sex'])
    smoking = int(request.form['smoking'])
    time = int(request.form['time'])

    values = [[age, anaemia, creatinine_phosphokinase, diabetes,ejection_fraction, high_blood_pressure, platelets,
                serum_creatinine, serum_sodium, sex, smoking, time]]
    print(values)

    print(clusterer.predict(values))
    cluster = clusterer.predict(values)
    prediction=-1
    if cluster == 0:
        prediction = RF_model1.predict(values)
    if cluster == 0:
        prediction = RF_model1.predict(values)
    print(prediction)
    if prediction == -1:
        statement = "You are at risk of heart attack"
    else:
        statement = "You are not at risk"
    # return " Prediction is: " + str(prediction)
    return render_template('results.html',statement=statement)



if __name__ == "__main__":
    app.run(host='0.0.0.0')

