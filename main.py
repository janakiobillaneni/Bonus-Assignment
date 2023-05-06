import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': 'cloudminion',
})

db = firestore.client()
def Call_Minions(request):
  minion_request = request.args

ref_minions = db.collection("Minion_Table")
minions = ref_minions.get()

list_of_minions = []
for doc in minions:
  list_of_minions.append(doc.to_dict())

minions_required = {}
for m in list_of_minions:
  if m["ID"] == int(minion_request["ID"]):
  minions_required = m
break
if not minions_required:
  return "Given Minion ID not available "

return minions_required
