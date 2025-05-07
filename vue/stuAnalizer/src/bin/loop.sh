#!/bin/bash
# DELETE_USERS=('adelisa.ibrisevic2' 'adelita.custic')
# echo $(date -u) 
# echo "Delete users: ${DELETE_USERS[@]} "
# for user in "${DELETE_USERS[@]}"
# do
#   echo "virtualmin delete-user --domain placa.studenac.hr --user $user &"
# done
# echo "running requests"

# nice / renice COMMAND
# cpulimit -l 50 COMMAND


while read -r line; do
  echo "virtualmin delete-user --domain placa.studenac.hr --user $line"
done < users.txt