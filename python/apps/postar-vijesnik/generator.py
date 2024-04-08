import csv
from helpers import csvStringToArray

domena="enatel.hr"
oldServer="178.63.74.244"

filename = domena.replace('.','_')
users =[]

def getEmails():
	with open('_src/'+ filename +'.csv', 'rt') as f:
		reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
	
		with open('_gen/' + filename +".md", "w") as text_file:
			
			text_file.write(f"# {domena}\n```\n")
			
			for row in reader:
				tmp = row[0].replace(';',':')
				users.append(tmp)
				text_file.write( tmp + '\n')
			
			text_file.write('```')
			text_file.write('\n\n---\n\n')

			for row in users:
				item = row.split(':')
				text_file.write('#' + item[0] + '\n')
				text_file.write(f"""```sh
/usr/bin/imapsync \\
  --host1 {oldServer} --user1 {item[0]}.{domena} --password1 '"{item[2]}"' \\
  --host2 localhost --user2 {item[0]}@{domena} --password2 '"{item[2]}"'
```\n
"""
)


#__main__
getEmails()
