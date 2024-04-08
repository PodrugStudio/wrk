import os, env
from usersAdd import INPUT_FILE
import helpers

INPUT_FILE = env.INPUT_FILE

errors = 0
badFormated = []

csvUsers = helpers.CheckCsvUsers(INPUT_FILE)

with open('report.csv', 'w', encoding='utf-8') as f:
	f.write ("?OK;id;uID;username;real name;=>;fixed username \n")
	idx=1
	for i in csvUsers:
		if any(c in "!@#$%^&*()[]{};:,/<>?\|`~-=_+ " for c in i['name']):
			# print (idx, i, '=>', helpers.CleanupUsername(i['name']))
			f.write (f"NOK\t{idx};{i['id']};{i['name']};{i['real']};=>;{helpers.CleanupUsername(i['name'])} \n")
		else:
			f.write (f"+OK\t{idx};{i['id']};{i['name']};{i['real']};--; OK\n")
		idx +=1
