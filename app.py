from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)


with open("weather_model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        humidity = float(request.form["humidity"])
        windspeed = float(request.form["windspeed"])
        pressure = float(request.form["pressure"])

        features = np.array([[humidity, windspeed, pressure]])
        prediction = model.predict(features)[0]

        return render_template(
            "index.html",
            prediction_text=f"Predicted Temperature: {prediction:.2f} °C"
        )
    except:
        return render_template(
            "index.html",
            prediction_text="Please enter valid input values"
        )

if __name__ == "__main__":
    app.run(debug=True)
