import fRadnici from '@/data/radnici.csv?raw'
import fHomes from '@/data/homes.txt?raw'

import { orderBy, includes, filter, find, replace, some } from 'lodash-es'

export interface RADNIK {
  id: String
  name: String
  fName: String
  lName: String
  username: String
  password: String
  hasHome: Boolean
  badUname: Boolean
  xlsActive: String
}

export interface HOME {
  dir: String
  hasUser: Boolean
  radnik: RADNIK
}

const radnici = [] as Array<RADNIK>
const RadniciData = fRadnici.split('\n')

RadniciData.forEach((radnik) => {
  const tmp = radnik.split(';')

  const objRadnik = {} as RADNIK
  if (tmp[0] && tmp[0] !== 'ID') {
    objRadnik.id = tmp[0]
    objRadnik.fName = tmp[1]
    objRadnik.lName = tmp[2]
    objRadnik.username = tmp[3]
    objRadnik.password = tmp[4]
    objRadnik.hasHome = includes(fHomes, objRadnik.username)
    objRadnik.badUname = includes(objRadnik.username, '..') || includes(objRadnik.username, ' ')
  }
  radnici.push(objRadnik)
})

const homes = [] as Array<HOME>
const homesWrk = fHomes.split('\n')
homesWrk.forEach((h) => {
  const tmp = {} as HOME
  tmp.dir = h
  tmp.radnik = find(radnici, (r: RADNIK) => r.username === h)
  tmp.hasUser = tmp.radnik ? true : false

  if (tmp.dir) homes.push(tmp)
})

export { radnici }
export { homes }
