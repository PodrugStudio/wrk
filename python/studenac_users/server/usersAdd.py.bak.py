import csv, json
#import env
import requests as req
from requests.auth import HTTPBasicAuth
from datetime import datetime

wrkPath = '/home/placa/public_html/Radnici/'
logPath = '/root/e1/crons/placa/logs/'
fileName = 'radnici.csv'
removeFilename="remove.csv"

authName='ivan'
authPass='ighMyDfBB3DdVb6YY6fX'

USER_DEFAULT_QUOTA='32000'


#csvUsers = {'name':csvUser[3], 'password':csvUser[4], 'real':realname.title()}
serverUsers, csvUsers, newUsers = [],[],[]
logFilePath = logPath + datetime.today().strftime('%Y%m') + '.log'
eventLog = {'date':datetime.today().strftime("%Y%m%d_%H%M%S"), 'usersAdded':0, 'usersExists':0, 'usersDelete':0, 'errors':0, 'error':[]}

#serverUsers=['prijem', 'test','anela.adzaga']
print(80*"-")


def getCurrentUsers():
	myurl = "https://placa.studenac.hr:10000/virtual-server/remote.cgi?program=list-users&domain=placa.studenac.hr&json=1&multiline&name-only"
	resp = req.get(myurl,auth = HTTPBasicAuth(authName,authPass))
	#resp.encoding = 'utf-8' # Optional: requests infers this internally
	return(resp.json())

def CreateUser(usrObject):
	myurl = f"https://placa.studenac.hr:10000/virtual-server/remote.cgi?program=create-user&domain=placa.studenac.hr&user={usrObject['name']}&pass={usrObject['password']}&quota={USER_DEFAULT_QUOTA}&real={usrObject['real']}"
	resp = req.get(myurl,auth = HTTPBasicAuth(authName,authPass))
	#print(resp.text)

# read CSV
def GetCsvUsers():
	with open(wrkPath + fileName, 'rt', encoding='utf-8') as f:
		reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
		for row in reader:
			if len(row) <= 0: #makni prazne redove
				continue

			csvUser = row[0].split(';')
			realname = csvUser[1] + ' ' + csvUser[2]
			if ('@' in csvUser[3]):
				eventLog['errors'] +=1
				eventLog['error'].append({'uId':csvUser[0], 'uName':csvUser[3], 'error':'@ in username'})
			else:
				if 'ID' not in csvUser[0]: #ignoriraj header red ako ga ima
					csvUsers.append(
						{'name':csvUser[3],
						'password':csvUser[4],
						'real':realname.title()})

# Write report
def WriteReport():
	with open(logFilePath, "a") as logFile:
		logFile.write(json.dumps(eventLog))
		logFile.write('\n')


# ---------------------------------
#		Main
# ---------------------------------

# fill Array with users
userList = getCurrentUsers()
for u in userList['data']:
	serverUsers.append(u['name'])

GetCsvUsers()

for u in csvUsers:
	if u['name'] not in serverUsers:
		newUsers.append(u)
		eventLog['usersAdded'] +=1
	else:
		eventLog['usersExists'] +=1

for u in newUsers:
	CreateUser(u)
WriteReport()
