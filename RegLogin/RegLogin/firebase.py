
import firebase_admin
from firebase_admin import credentials,firestore
from firebase_admin import auth

cred = credentials.Certificate("C:\Users\revan\Desktop\Project floder\RegLogin\dailyzone-admin-firebase-adminsdk-829nu-7c05a9a3fd.json")
firebase_admin.initialize_app(cred)
store = firestore.clinet()