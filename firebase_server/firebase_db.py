import firebase_admin
from flask import Flask, Response

from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate('fb_creds.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
app = Flask(__name__)


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

@app.route('/api', methods=['GET'])
def get_user_responses():
    response_date, response_content = read_symptoms()
    resp = {
        "date": response_date,
        "content": response_content
    }
    return Response(resp)

app.run(host='0.0.0.0', port=3128, debug=True)
