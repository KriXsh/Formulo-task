## formulo task  -------------------------------------------------------------------------------------------------------------------------------------------------------
# Backend - doctor-patient-backend

This project contains a full-stack application with a Flask backend and a React frontend.

## Prerequisites

- Python 3.x
- Node.js and npm

- ```bash
- cd doctor-patient-dashboard

## Setup
The backend is implemented using Flask and connects to a MongoDB database. It provides two main endpoints:
## Test Run command : python app.py

Accessing the Application
The backend will run on http://127.0.0.1:5000.


## curls 
## get the all patients
1. curl --location 'http://127.0.0.1:5000/patients'
2. curl --location 'http://127.0.0.1:5000/patients?date=2024-06-05'

*  /patients (GET): Fetches a list of patients with appointments on a specified date.

3. curl --location 'http://127.0.0.1:5000/patients/chat-history' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Rishabh Jain"
}'

* /patients/chat-history (POST): Fetches the chat history and message count for a specified patient.

## Backend Code Explanation
The backend is implemented using Flask and connects to a MongoDB database. It provides two main endpoints:

/patients (GET): Fetches a list of patients with appointments on a specified date.
/patients/chat-history (POST): Fetches the chat history and message count for a specified patient.



## Frontend - doctor-patient-dashboard ----------------------------------------------------------------------------------------------------------------------------------

cd ./doctor-patient-dashboard

## Install the required packages:
- npm install

## Start the React application:
- npm start

* Accessing the Application
The frontend will run on http://localhost:3000.

## Frontend Code Explanation
The frontend is implemented using React and styled with Bootstrap. It allows users to:

View a list of patients in a card layout.
Select a date to filter patients by their next appointment.
Click on a patient card to view their chat history and message count.

