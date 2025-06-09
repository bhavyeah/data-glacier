from flask import Flask, request, render_template, jsonify
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = np.array([float_features])
    prediction = model.predict(features)
    return render_template("index.html", prediction_text=f"Predicted Class: {prediction[0]}")

@app.route("/api", methods=["POST"])
def api_predict():
    data = request.get_json(force=True)
    prediction = model.predict([np.array(data["features"])])
    return jsonify({"prediction": prediction.tolist()})

if __name__ == "__main__":
    app.run(debug=True)
