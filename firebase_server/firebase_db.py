import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate('fb_creds.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


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

print(read_symptoms())
