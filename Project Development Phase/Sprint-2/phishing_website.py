from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn import metrics 
import warnings
import pickle
warnings.filterwarnings('ignore')

import pickle
pickle.dump(open("Model building.pkl", "wb"))



app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def web_detection():
    if request.method == "POST":

        url = request.form["url"]
        
        x = np.array.reshape(1,30) 

        y_pred =web_detection.predict(x)[0]
        #1 is safe       
        #-1 is unsafe
        y_pro_phishing = web_detection.predict_proba(x)[0,0]
        y_pro_non_phishing = web_detection.predict_proba(x)[0,1]
        # if(y_pred ==1 ):
        pred = "It is {0:.2f} % safe to go ".format(y_pro_phishing*100)
        return render_template('web detection.html',xx =round(y_pro_non_phishing,2),url=url )
    return render_template("web detection.html", xx =-1)


if __name__ == '__main__':
    app.run (host='0.0.0.0', debug=True)
