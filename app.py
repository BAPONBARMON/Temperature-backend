from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # To allow frontend to access this backend

API_KEY = "ff7060f17d6e703503cd83a51fbec078"

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City is required'}), 400

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200 or data.get("cod") != 200:
            return jsonify({'error': 'City not found'}), 404

        return jsonify({
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()