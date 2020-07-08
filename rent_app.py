import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle

app = Flask(__name__)
model = pickle.load(open('Brazil_Rent_Predictor.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('contact.html')

@app.route('/predict', methods = ['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    print(prediction[0])
    
    return render_template('contact.html', prediction_text="API for Jaipir {}".format(prediction[0]))

@app.route('/predict_api', methods=['POST'])
def predict_api():
    '''
    For direct API calls through request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])
    
    output = prediction[0]
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)
    