import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime
import json
cred = credentials.Certificate('motvial-mixed-firebase-adminsdk-vaqdv-66ae1bdbc4.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def newFailure(id,location,severity,solved):
    global db
    time = datetime.now()
    fallo = db.collection('failures').document(id)
    data = {
        'failure_date': time.strftime("%d/%m/%Y %H:%M:%S"),
        'location': location,
        'severity': severity,
        'solved': solved,
        'solved_date': time.strftime("%d/%m/%Y %H:%M:%S")
    }
    fallo.set(data)

