import csv, json
import env
import requests as req
from requests.auth import HTTPBasicAuth
from datetime import datetime

wrkPath = '/home/placa/public_html/Radnici/'
logPath = '/root/e1/crons/placa/logs/'
fileName = 'radnici.csv'
removeFilename="remove.csv"

serverUsers, csvUsers, newUsers = [],[],[]
logFilePath = logPath + datetime.today().strftime('%Y%m') + '.log'
eventLog = {'date':datetime.today().strftime("%Y%m%d_%H%M%S"), 'usersAdded':0, 'usersExists':0, 'usersRemoved':0, 'errors':0, 'error':[]}

print (80*'=')

def RemoveUser(username):
	myurl = f"https://placa.studenac.hr:10000/virtual-server/remote.cgi?program=delete-user&domain=placa.studenac.hr&user={username}"
	resp = req.get(myurl,auth = HTTPBasicAuth(env.authName,env.authPass))
	return(resp.text)

# read CSV
def GetCsvUsers():
	with open(env.wrkPath + env.removeFilename, 'rt', encoding='utf-8') as f:
		reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
		for row in reader:
			if len(row) <= 0: #makni prazne redove
				continue

			csvUser = row[0].split(';')
			if ('@' in csvUser[3]):
				eventLog['errors'] +=1
				eventLog['error'].append({'uId':csvUser[0], 'uName':csvUser[3], 'error':'@ in username'})
			else:
				if 'ID' not in csvUser[0]: #ignoriraj header red ako ga ima
					csvUsers.append(
						{'name':csvUser[3]})
				

# Write report
def WriteReport():
	with open(logFilePath, "a") as logFile:
		logFile.write(json.dumps(eventLog))
		logFile.write(',\n')

# ------------------------------------------------------
#		Main
# ------------------------------------------------------

GetCsvUsers()

for u in csvUsers:
	response = RemoveUser(u['name'])
	if 'Exit status: 0' in response: # 0 = OK
		eventLog['usersRemoved'] +=1
		print("removed", ['name'])
	else:
		eventLog['errors'] +=1
		eventLog['error'].append(response) #256 no such user
		print("skipped",u['name'])

WriteReport()
print ("done")
