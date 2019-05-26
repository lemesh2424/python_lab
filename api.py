from flask import Flask, request
from flask_restful import Resource, Api
from serialization import Serialization
from fuel import Fuel

s = Serialization()

station = s.load()

app = Flask(__name__)
api = Api(app)


class Station(Resource):
    def get(self):
        return s.load_json(), 200

    def post(self):
        obj = request.form
        station.add_fuel_type(Fuel(obj["name"], int(obj["tank"])))
        s.save(station)
        return s.load_json(), 201

    def put(self):
        obj = request.form
        station.spend_fuel(obj["name"], int(obj["tank"]))
        s.save(station)
        return s.load_json(), 200

    def delete(self):
        obj = request.form["name"]
        station.delete_fuel_type(obj)
        s.save(station)
        return s.load_json(), 200


api.add_resource(Station, '/')

if __name__ == '__main__':
    app.run(debug=True)
