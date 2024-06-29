from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/save-location', methods=['POST'])
def save_location():
    data = request.json
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    if latitude and longitude:
        with open('locations.txt', 'a') as file:
            file.write(f"Latitude: {latitude}, Longitude: {longitude}\n")
        return jsonify({"status": "success"}), 200
    else:
        return jsonify({"status": "error", "message": "Invalid data"}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
