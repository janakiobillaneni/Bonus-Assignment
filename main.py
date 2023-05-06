import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': 'cloudminion',
})

db = firestore.client()
def Call_Minions(request):
  minionrequest = request.args

ref_minions = db.collection("Minion_Table")
minions = ref_minions.get()

lstminions = []
for doc in minions:
  lstminions.append(doc.to_dict())

minionsreq = {}
for m in lstminions:
  if m["ID"] == int(minionrequest["ID"]):
  minionsreq = m
break
if not minionsreq:
  return "Given Minion ID not available "

return minionsreq
