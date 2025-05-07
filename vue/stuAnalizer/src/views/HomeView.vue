<script setup lang="ts">
interface RADNIK {
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

import { orderBy, includes, filter, find, replace } from 'lodash-es'

import fRadnici from '@/data/radnici.csv?raw'
import fHomes from '@/data/homes.txt?raw'
import fAktivni from '@/data/aktivni240531.csv?raw'
import { reactive } from 'vue'

const HomesData = fHomes.split('\n')
const RadniciData = fRadnici.split('\n')
const AktivniData = fAktivni.split('\n')

const radnici = [] as Array<RADNIK>
const xlsRadnici = [] as Array<RADNIK>

AktivniData.forEach((radnik) => {
  const tmp = radnik.split(';')
  const objRadnik = {} as RADNIK
  if (tmp[1] && tmp[1] !== 'ID') {
    objRadnik.id = tmp[1]
    objRadnik.name = tmp[0]

    xlsRadnici.push(objRadnik)
  }
})

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
    objRadnik.xlsActive = find(xlsRadnici, { id: objRadnik.id })
  }
  radnici.push(objRadnik)
})

const analiza = reactive({
  noHost: filter(radnici, function (r: RADNIK) {
    return !r.hasHome
  }).length,
  badUname: filter(radnici, function (r: RADNIK) {
    return r.badUname
  }).length
})

function checkValidHost(uName: String) {
  let test = uName.replace(' ', '.')
  test = replace(test, '-', '')
  test = replace(test, '..', '.')
  test = replace(test, '..', '.')

  // console.table([uName, test, includes(HomesData, test)])
  const hasFixedHome = includes(HomesData, test) as Boolean

  return (hasFixedHome ? '✔️ ' : '❌ ') + test
}
</script>

<template>
  <aside>
    <h1>Analiza</h1>
    <h2>Hosted</h2>
    <ul>
      <li>Total disk: {{ HomesData.length }}</li>
      <li>Višak korisnika: {{ HomesData.length - radnici.length }}</li>
      <!-- <li>Total webmin:</li> -->
    </ul>
    <hr />
    <h2>Radnici.csv</h2>
    <ul>
      <li>📪 Ukupno: {{ radnici.length }}</li>
      <li>🐞 Nepostavljenih: {{ analiza.noHost }}</li>
      <li>🔥 Bad usernames: {{ analiza.badUname }}</li>
    </ul>
    <hr />
    <h2>Dostavljeni XLS</h2>
    <ul>
      <li>📊 Ukupno: {{ xlsRadnici.length }}</li>
      <li>⚪️ Nedostaje: {{ radnici.length - xlsRadnici.length }}</li>
    </ul>
  </aside>
  <main>
    <table>
      <tr>
        <th>idx</th>
        <th>ID</th>
        <th>uName</th>
        <th>📪</th>
        <th>🔥</th>
        <th>≈</th>
        <th>📊</th>
      </tr>
      <tr
        v-for="(radnik, idx) in orderBy(radnici, ['hasHome', 'badUname'], ['asc', 'desc'])"
        :key="`radnik${idx}`"
      >
        <td>{{ idx + 1 }}</td>
        <td>{{ radnik.id }}</td>
        <td>{{ radnik.username }}</td>
        <td>{{ radnik.hasHome ? '✅' : '🐞' }}</td>
        <td>{{ radnik.badUname ? '🔥' : '' }}</td>
        <td>{{ radnik.badUname ? checkValidHost(radnik.username) : '' }}</td>
        <td>{{ radnik.xlsActive ? '🟢 ' + radnik.xlsActive.name : '⚪️' }}</td>
      </tr>
    </table>
  </main>
</template>

<style lang="scss">
table {
  border-right: 1px solid #0002;
  border-top: 1px solid #0002;
}
th {
  padding: 4px;
  font-weight: 800;
  border-left: 1px solid #0002;
  border-bottom: 2px solid #0004;
}
td {
  padding: 4px;
  font-size: 19px;

  border-left: 1px solid #0002;
  border-bottom: 1px solid #0002;
}
</style>
