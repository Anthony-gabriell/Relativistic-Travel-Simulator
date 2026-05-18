from flask import Flask, jsonify, request
from physics import *
from destinations import get_destinations, get_distance
from flask_cors import CORS

app = Flask(__name__)

app = Flask(__name__)
CORS(app)

@app.route('/destinations', methods=['GET'])
def destinations():
    return jsonify(get_destinations())

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    destine = data['destine']
    velocity = float(data['velocity'])

    if not validate_velocity(velocity):
        return jsonify({'error': 'Invalid velocity. Must be between 0 and 1.'}), 400

    result_destine = get_distance(destine)
    distance = result_destine[1]

    return jsonify({
        'lorentz_factor': lorentz_factor(velocity),
        'time_on_earth': time_on_earth(distance, velocity),
        'time_for_traveler': time_for_traveler(distance, velocity),
        'contracted_distance': contracted_distance(distance, velocity),
        'relativistic_energy': relativistic_energy(velocity, 1)
    })

if __name__ == '__main__':
    app.run(debug=True)

