from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def get_temperature():
    city = request.args.get("city")
    # Dummy data for now
    temp_data = {
        "Lanka": "34°C",
        "Delhi": "37°C",
        "Kolkata": "33°C"
    }
    temperature = temp_data.get(city, "Not Found")
    return jsonify({
        "city": city,
        "temperature": temperature
    })

if __name__ == "__main__":
    app.run()
