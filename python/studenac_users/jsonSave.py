import pathlib
import json
from json.decoder import JSONDecodeError
from datetime import datetime

#LOG_FILENAME = 'data.json'
LOG_FILENAME = 'logs/gen/' + datetime.today().strftime('%Y%m') + '.log'

a_dictionary = {"init": 2}

if not pathlib.Path(LOG_FILENAME).exists():
	open(LOG_FILENAME, mode='w')

with open(LOG_FILENAME, mode='r+', encoding='utf-8') as jsonFile:
	try:
		jsonData = json.load(jsonFile)
		jsonData["events"].append(a_dictionary)
	except JSONDecodeError:
		jsonData = {"events":[]}
		jsonData["events"].append(a_dictionary)

with open(LOG_FILENAME, mode='w', encoding='utf-8') as jsonFile:
	json.dump(jsonData, jsonFile)
