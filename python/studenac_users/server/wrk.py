from http import server
import os, env
import helpers

print(80*'=')

# serverUsers = helpers.GetCurrentUsers('local')
serverUsers = helpers.GetCurrentUsers()
totalServerUsers = len(serverUsers)

csvUsers = helpers.GetCsvUsers(env.FILE_RADNICI_CSV)
newUsers = helpers.UsersToAdd(serverUsers, csvUsers)

if len(newUsers) > 0:
	print(80*'-')
	for idx, u in enumerate(newUsers):
		print (f'[{idx+1}/{len(newUsers)}]\t',u['name'])
	print(80*'=')

csvRemoveUsers = helpers.GetCsvUsers(env.FILE_REMOVE_CSV)
usersToRemove = helpers.UsersToRemove(serverUsers, csvRemoveUsers)

if len(usersToRemove) > 0:
	print(80*'-')
	for idx, u in enumerate(usersToRemove):
		print (f'[{idx+1}/{len(usersToRemove)}]\t',u['name'])
	print(80*'=')


print ("Total server users:\t", totalServerUsers)
print ("radnici.csv:\t\t", len(csvUsers))
print ("remove.csv:\t\t", len(csvRemoveUsers))
print(80*'-')
print ("Total ADD users:\t", len(newUsers))
print ("Total DEL users:\t", len(usersToRemove))
print(80*'=')

print("DONE")
