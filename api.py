from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# client = MongoClient("mongodb+srv://berthnk:<Abigaelisa49>@smart-devices.wqoztxy.mongodb.net/?retryWrites=true&w=majority")
client = MongoClient("mongodb://127.0.0.1:27017/")

db = client["smart-lights"]
lights_collection = db["lights"]

initial_lights_data = [
    {"location": "kitchen", "state": False},
    {"location": "bathroom", "state": False},
    {"location": "bedroom", "state": False},
    {"location": "living_room", "state": False},
    {"location": "veranda", "state": False},
]

if lights_collection.count_documents({}) == 0:
    lights_collection.insert_many(initial_lights_data)

@app.route('/toggle_light', methods=['POST'])
def toggle_light():
    data = request.get_json()
    location = data.get("location")

    if location:
        light = lights_collection.find_one({"location":location})

        if light:
            new_state = not light["state"]
            lights_collection.update_one({"location":location}, {"$set": {"state":new_state}})
            return jsonify({"success": True, "location": location, "state": new_state})
        else:
            return jsonify({"success": False, "message": f"Light in {location} not found"}), 404
    else:
        return jsonify({"success": False, "message": "Location not provided in request"}), 400
    
@app.route('/get_lights', methods=['GET'])
def get_lights():
    lights_data = list(lights_collection.find({}, {"_id": 0}))
    return jsonify(lights_data)

if __name__ == '__main__':
    app.run(debug=True)
