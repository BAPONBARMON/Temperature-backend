from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

API_KEY = "46ef8d93c0414f0f85f123007252506"

@app.route("/", methods=["GET"])
def get_temperature():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "City not provided"}), 400

    # OpenWeatherMap API URL
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(weather_url)
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            return jsonify({
                "city": city,
                "temperature": f"{temp}°C"
            })
        else:
            return jsonify({
                "city": city,
                "temperature": "City not found."
            }), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()
