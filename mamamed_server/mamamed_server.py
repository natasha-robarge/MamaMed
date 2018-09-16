import json
import ssl
import firebase_admin

from firebase_admin import credentials
from firebase_admin import firestore
from flask import Flask, request, Response


cred = credentials.Certificate('fb_creds.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
app = Flask(__name__)

cert_file = 'rootCA.pem'
pkey_file = 'server.key'
context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.load_cert_chain(cert_file, pkey_file)

def read_symptoms():
   users_ref = db.collection('test')
   docs = users_ref.get()
   symptoms = []
   for doc in docs:
       doc = doc.to_dict()
       split_doc = doc['entry'].split('|')
       if len(split_doc) > 1:
           symptoms.append([split_doc[1], split_doc[0]])
   return symptoms

MOCK_DATA = [
    {
        "patientId" : 1,
        "patientInfo" : {
            "name": "Sandy Payne",
            "dateOfBirth": "1980-07-09",
            "age": 38,
            "pregnancyStartDate": "2018-04-01",
            "dateOfLastPeriod": "2017-03-25",
            "dueDate": "2019-01-06",
        },
        "medications" : [
            {
                "name": "prenatal vitamins",
                "prescribedBy": "Dr. Timber",
                "startDate": "2018-01-01 18:00:00 CDT",
                "stopDate": "2019-01-06 18:00:00 CDT"
            },
            {
                "name":"secondMedA",
                "prescribedBy": "doctorA",
                "startDate": "2018-09-02 18:00:00 CDT",
                "stopDate": "2018-09-02 18:00:00 CDT"
            }
        ],
        "diagnoses" : [
            {
                "description": "description given by doctor from one apptA",
                "doctorNameA": "Doctor A",
                "diagnosisDate": "2018-03-02 18:00:00 CDT"
            }, {
                "description": "description from another apptA",
                "doctorNameA": "Doctor A",
                "diagnosisDate": "2018-03-02 18:00:00 CDT"
            }
        ],
        "appointments": [
            {
                "date": "2018-09-01 10:00:00 CST",
                "doctorName": "Nurse A",
                "doctorTitle": "Nurse",
                "comment": "Patient said they experienced dizziness when standing up"
            }, 
            {
                "date": "2018-06-05 10:00:00 CST",
                "doctorName": "Nurse A",
                "doctorTitle": "Nurse",
                "comment": "Patient said they were experiencing frequent headaches"
            }
        ],
        "patientGoogleVoiceSessions" : read_symptoms()
    }
]


@app.route('/mamamed', methods=['GET', 'OPTIONS'])
def main():
    resp = Response("hi")
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    resp.headers['Cache-Control'] = 'no-cache'
    return resp


@app.route('/mamamed/patient/<int:id>', methods=['GET', 'OPTIONS'])
def getAllPatientInfo(id):
    # resp = Response("Foo bar baz")
    resp = Response(json.dumps(MOCK_DATA))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    resp.headers['Content-Type'] = 'application/json'
    resp.headers['Cache-Control'] = 'no-cache'
    print(resp)
    return resp


"""
Creates a new appointment or updates an existing one for a patient (specified by patient_id)
and returns a list of all past and upcoming appointments. Required fields for new appointments:
appointment time and doctor name.

Example appointment info:
{
    "date": "2018-06-05 10:00:00 CST",
    "doctorName": "Nurse A",
    "doctorTitle": "Nurse",
    "comment": "Patient said they were experiencing frequent headaches"
}
"""
@app.route('/mamamed/appointments/<int:patient_id>', methods=['POST', 'OPTIONS'])
def createOrUpdateAppointment(patient_id):
    # TODO:  look up patient appointments by id
    reqJson = request.get_json()
    print(reqJson)

    # TODO:  check if appointment already exists, update if so instead of creating new one

    date = reqJson.get("date", "")
    doctorName = reqJson.get("doctorName", "")

    if not len(date) or not len(doctorName):
        return Response("Please enter an appointment time and doctor name.", status=404)

    doctorTitle = reqJson.get("doctorTitle", "")
    comment = reqJson.get("comment", "")
    new_appointment = {
        "date": date,
        "doctorName": doctorName,
        "doctorTitle": doctorTitle,
        "comment": comment
    }
    MOCK_DATA[0]["appointments"].append(new_appointment)

    resp = Response(json.dumps(MOCK_DATA[0]["appointments"]))
    return resp


app.run(host='0.0.0.0', port=5000, debug=True, ssl_context=context)
