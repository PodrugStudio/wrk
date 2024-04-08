import os, env
import helpers

serverUsers = helpers.GetCurrentUsers('local')
totalServerUsers = len(serverUsers)
csvUsers = helpers.GetCsvUsers(env.FILE_RADNICI_CSV)
newUsers = helpers.UsersToAdd(serverUsers, csvUsers)

print(f"""
ADD USERS INFO
{80*'-'}
Total server users:\t {totalServerUsers}
Total CSV users:\t {len(csvUsers)}
Total NEW users:\t {len(newUsers)}
{80*'-'}""")

if len(newUsers) > 0:
	print("Adding new users...", "\n", 80*'-')
	for idx, u in enumerate(newUsers):
		# print (f'[{idx+1}/{len(newUsers)}]\t',u['name'], helpers.CreateUser(u))
		print (f'[{idx+1}/{len(newUsers)}]\t',u['name'])
else:
	print ("No new users to add.")

print(80*'=')
print("DONE")
