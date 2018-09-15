import json
from bottle import route, run

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

@route('/mamamed', method='GET')
def main():
    return "hi\n"

@route('/mamamed/patient/<id>', method='GET')
def getAllPatientInfo(id):
    return json.dumps(MOCK_DATA)


run(host='0.0.0.0', port=8080, debug=True)
