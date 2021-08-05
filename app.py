from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('logistic_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        apr= float(request.form['apr'])
        ssnLoanCount=int(request.form['ssnLoanCount'])
        nPaidOff=float(request.form['nPaidOff'])
        log_nPaidOff= np.log(nPaidOff+1)
        loanAmount=float(request.form['loanAmount'])
        log_loanAmount= np.log(loanAmount+1)
        clearfraudscore = float(request.form['clearfraudscore'])

        payFrequency = request.form['payFrequency']
        if(payFrequency=='B'):
                payFrequency_B=1
                payFrequency_W=0
                payFrequency_I=0
                payFrequency_M=0
                payFrequency_S=0
        elif(payFrequency=='W'):
                payFrequency_W=1
                payFrequency_B=0
                payFrequency_I=0
                payFrequency_M=0
                payFrequency_S=0
        elif(payFrequency=='I'):
                payFrequency_I=1
                payFrequency_B=0
                payFrequency_W=0
                payFrequency_M=0
                payFrequency_S=0
        elif(payFrequency=='M'):
                payFrequency_M=1
                payFrequency_B=0
                payFrequency_I=0
                payFrequency_W=0
                payFrequency_S=0
        else:
                payFrequency_B=0
                payFrequency_I=0
                payFrequency_W=0
                payFrequency_S=1
                payFrequency_M=0

        prediction=model.predict([[apr, clearfraudscore, ssnLoanCount, log_loanAmount, log_nPaidOff, payFrequency_B, payFrequency_I, payFrequency_M, payFrequency_S, payFrequency_W]])
        
        if (prediction==0):
            return render_template('index.html',prediction_text="Congratulations!!  You are eligible for the loan.")
        else:
            return render_template('index.html',prediction_text="Oops!! You are not eligible for the loan, try again in future.")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

