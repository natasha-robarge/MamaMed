import json
import ssl
from flask import Flask, Response

MOCK_DATA = [
    {
        "patientId" : 1,
        "patientInfo" : {
            "name": "daenerys",
            "age": 25,
            "pregnancyStartDate": "2018-01-01"
        },
        "medications" : [
            {
                "name": "firstMedA",
                "prescribedBy": "doctorA",
                "startDate": "2018-09-02 18:00:00 CDT",
                "stopDate": "2018-09-02 18:00:00 CDT"
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
        ]
    }
]

app = Flask(__name__)

cert_file = 'rootCA.pem'
pkey_file = 'server.key'
context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.load_cert_chain(cert_file, pkey_file)


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

app.run(host='0.0.0.0', port=5000, debug=True, ssl_context=context)
