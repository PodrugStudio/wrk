import csv, json, re
import env
import requests as req
from requests.auth import HTTPBasicAuth

def csvStringToArray(string,delimiter=","):
	return [int(e) if e.isdigit() else e for e in string.split(delimiter)]

def CleanupUsername(u, _isUsername = True):
	# replace fckedup chars with space
	u = u.translate ({ord(c): " " for c in "!@#$%^&*()[]{};:,/<>?\|`~-=_+"})

	# fix double dots
	u = re.sub('\.+', ' ', u)

	# multiple spaces => one space
	u = re.sub(' +', ' ', u)

	# replace space with dot
	if _isUsername:
		u = u.replace(' ', '.')
	return u

def GetCurrentUsers( _type = 'server'):

	serverUsers=[]

	if _type == 'server':
		myurl = "https://placa.studenac.hr:10000/virtual-server/remote.cgi?program=list-users&domain=placa.studenac.hr&json=1&multiline&name-only"
		resp = req.get(myurl,auth = HTTPBasicAuth(env.authName,env.authPass))
		resp.encoding = 'utf-8' # Optional: requests infers this internally
		
		for su in resp.json()['data']:
			serverUsers.append(su['name'])

	if _type == 'local':
		jsonData = json.load(open('ulaz/remote.json'))['data']
		for su in jsonData:
			serverUsers.append(su['name'])

	return serverUsers

def GetCsvUsers( INPUT_FILE ):
	csvUsers = []
	with open( INPUT_FILE , 'rt', encoding='utf-8') as f:
		reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
		for row in reader:
			if len(row) <= 0: #makni prazne redove
				continue

			csvUser = row[0].split(';')
			realname = CleanupUsername(csvUser[1], False) + ' ' + CleanupUsername(csvUser[2], False)
			fixedUName = CleanupUsername(csvUser[3])
			if 'ID' not in csvUser[0]: #ignoriraj header red ako ga ima
				csvUsers.append(
					{'name':fixedUName,
					'password':csvUser[4],
					'real':realname.title()})
	
	return csvUsers

def UsersToAdd( _serverUsers, _csvUsers):
	processUsers=[]
	for u in _csvUsers:
		unixUsername = u['name'] + "@placa.studenac.hr"
		# #name responsa se promijenio iz name.lastname u name.lastname@placa.studenac.hr
		# if u['name'] not in _serverUsers:
		if unixUsername not in _serverUsers:
			processUsers.append(u)

	return processUsers

def UsersToRemove( _serverUsers, _csvUsers):
	processUsers=[]
	for u in _csvUsers:
		unixUsername = u['name'] + "@placa.studenac.hr"
		# if u['name'] in _serverUsers:
		if unixUsername in _serverUsers:
			processUsers.append(u)

	return processUsers

def CreateUser(usrObject):
	myurl = f"https://placa.studenac.hr:10000/virtual-server/remote.cgi?program=create-user&domain=placa.studenac.hr&user={usrObject['name']}&pass={usrObject['password']}&quota={env.USER_DEFAULT_QUOTA}&real={usrObject['real']}"
	resp = req.get(myurl,auth = HTTPBasicAuth(env.authName,env.authPass))
	return (resp.text)

def RemoveUser(username):
	myurl = f"https://placa.studenac.hr:10000/virtual-server/remote.cgi?program=delete-user&domain=placa.studenac.hr&user={username}"
	resp = req.get(myurl,auth = HTTPBasicAuth(env.authName,env.authPass))
	return(resp.text)


def CheckCsvUsers( INPUT_FILE ):
	csvUsers = []
	with open( INPUT_FILE , 'rt', encoding='utf-8') as f:
		reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
		for row in reader:
			if len(row) <= 0: #makni prazne redove
				continue

			csvUser = row[0].split(';')
			realname = csvUser[1] + ' ' + csvUser[2]
			fixedUName = csvUser[3]
			if 'ID' not in csvUser[0]: #ignoriraj header red ako ga ima
				csvUsers.append(
					{'id':csvUser[0],
					'name':fixedUName,
					'password':csvUser[4],
					'real':realname.title()})
	
	return csvUsers
