from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
client = MongoClient("mongodb+srv://assesment_user:uYdY!7f9C-HnX%40Y@cluster0.vcxxyf3.mongodb.net/Formulo_assesment")
db = client["Formulo_assesment"]
collection = db["patient-gateway"]

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return super().default(o)

app.json_encoder = JSONEncoder   ##to handle the the json response

def convert_objectid(data):
    if isinstance(data, list):
        return [convert_objectid(item) for item in data]
    elif isinstance(data, dict):
        return {key: convert_objectid(value) for key, value in data.items()}
    elif isinstance(data, ObjectId):
        return str(data)
    else:
        return data


@app.route('/patients', methods=['GET'])
def get_patients():
    date_str = request.args.get('date')
    query = {}
    if date_str:
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d')
            start_of_day = datetime(date.year, date.month, date.day)
            end_of_day = datetime(date.year, date.month, date.day, 23, 59, 59)
            query = {"next_appointment": {"$gte": start_of_day, "$lte": end_of_day}}
            print(f"Querying for date range: {start_of_day} to {end_of_day}")
        except ValueError:
            return jsonify({"error": "Invalid date format"}), 400

    patients = list(collection.find(query))
    print(f"Query: {query}")
    print(f"Patients found: {patients}")
    patients = convert_objectid(patients)
    return jsonify(patients)


@app.route('/patients/chat-history', methods=['POST'])
def get_chat_history():
    patient_name = request.json['name']
    patient = collection.find_one({"patient_name": patient_name})
    if patient:
        chat_history = patient.get('message', [])
        patient_messages = [msg for msg in chat_history if msg['sender'] == 'patient']
        response = {
            "chat_history": convert_objectid(chat_history),
            "patient_message_count": len(patient_messages)
        }
        return jsonify(response)
    return jsonify({"error": "Patient not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
