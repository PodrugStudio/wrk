from http import server
import os, env
import helpers

INPUT_FILE = env.INPUT_FILE

print(80*'=')

serverUsers = helpers.GetCurrentUsers('local')
totalServerUsers = len(serverUsers)

csvRemoveUsers = helpers.GetCsvUsers(env.INPUT_FILE_REMOVER)
usersToRemove = helpers.UsersToRemove(serverUsers, csvRemoveUsers)


for idx, u in enumerate(usersToRemove):
	print (f'[{idx+1}/{len(usersToRemove)}]\t',u['name'], helpers.RemoveUser(u['name']))
	# print (f'[{idx+1}/{len(usersToRemove)}]\t',u['name'])
