import os, env
import helpers

serverUsers = helpers.GetCurrentUsers('local')
csvRemoveUsers = helpers.GetCsvUsers(env.FILE_REMOVE_CSV)
usersToRemove = helpers.UsersToRemove(serverUsers, csvRemoveUsers)

print(f"""
DEL USERS INFO
{80*'-'}
Total server users:\t {len(serverUsers)}
Total CSV users:\t {len(csvRemoveUsers)}
Total DEL users:\t {len(usersToRemove)}
{80*'-'}""")

if len(usersToRemove) > 0:
	print("Adding new users...", "\n", 80*'-')
	for idx, u in enumerate(usersToRemove):
		# print (f'[{idx+1}/{len(usersToRemove)}]\t',u['name'], helpers.RemoveUser(u['name']))
		print (f'[{idx+1}/{len(usersToRemove)}]\t',u['name'])
else:
	print ("No users to remove.")

print(80*'=')
print("DONE")
