from flask import Flask
from flask_cors import CORS
from routes.patient_routes import register_patient_routes

app = Flask(__name__)

CORS(app)

register_patient_routes(app)

@app.route("/")
def home():
    return {"message": "Backend is running on port "}

if __name__ == "__main__":
    app.run(debug=True)
