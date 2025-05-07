<template>
  <aside>
    <h2>ADMINISTRACIJA</h2>
    <div>Ukupno korisnika: {{ users.length || 'UČITAVAM PODATKE...' }}</div>
    <input v-model="filterValue" type="text" placeholder="Search" />
    <hr width="100%" />
    <section v-if="review.duplicatedIds.length">
      <h4>Duplicirani ključevi</h4>
      <ul>
        <li
          v-for="dup in review.duplicatedIds"
          :key="`dup${dup}`"
          @click="filterValue = dup"
          class="ux-clickable"
        >
          {{ dup }}
        </li>
      </ul>
    </section>
    <section v-if="review.badUname.length">
      <h4>BAD UNAMES</h4>
      <ul>
        <li
          v-for="bname in review.badUname"
          :key="bname"
          @click="filterValue = bname"
          class="ux-clickable"
        >
          {{ bname }}
        </li>
      </ul>
    </section>
  </aside>
  <main>
    <!-- <div v-for="user in users" :key="user.ID">
      {{ user.ID }} | {{ user.eMail }} | {{ user.fullName }}
    </div> -->
    <EasyDataTable :headers="edtHeaders" :items="filteredUsers" alternating>
      <!-- <template #loading>
        <h3>Dohvaćam podatke...</h3>
      </template> -->
      <template #empty-message>
        <h3>Dohvaćam podatke...</h3>
      </template>
    </EasyDataTable>
  </main>
</template>

<script setup lang="ts">
import axios from 'axios'
import { ref, reactive, computed } from 'vue'
import { includes, filter, map } from 'lodash-es'
import type { Header /*, Item , SortType */ } from 'vue3-easy-data-table'

interface IUser {
  ID: string
  Ime: string
  Prezime: string
  fullName: string
  searchable: string
  eMail: string
  Lozinka: string
}

// const edtSortBy: string[] = ['ID', 'fullName']
// const edtSortType: SortType[] = ['asc', 'asc']
const edtHeaders: Header[] = [
  { text: 'ID', value: 'ID', sortable: true, width: 120 },
  { text: 'NAME', value: 'fullName', sortable: true },
  { text: 'UNAME', value: 'eMail' },
  { text: 'LOZINKA', value: 'Lozinka' }
]

const users = ref([] as Array<IUser>)

const filterValue = ref('')
const filteredUsers = computed(() =>
  filter(users.value, function (u: IUser) {
    return includes(u.searchable.toLowerCase(), filterValue.value.toLowerCase())
  })
)

axios
  .get('http://placa.studenac.hr/app/apiproba/users')
  .then((response) => {
    response.data.forEach((usr: IUser) => {
      usr.fullName = usr.Ime + ' ' + usr.Prezime
      usr.searchable = [usr.ID, usr.Ime, usr.Prezime, usr.eMail].join(' ')
    })
    users.value = response.data
    review.ids = map(users.value, 'ID')
    review.duplicatedIds = filter(review.ids, (val: string, i: number, iteratee: string) =>
      includes(iteratee, val, i + 1)
    )
    const unames = map(users.value, 'eMail')
    review.badUname = filter(unames, (usr: string) => includes(usr, '..') || includes(usr, ' '))
  })
  .catch((error) => {
    console.error('There was an error!', error)
  })

// WIP
const review = reactive({
  ids: [],
  duplicatedIds: [],
  badUname: []
})
// console.log(xor(...users.value.map((u) => [u])))
</script>

<style lang="scss">
aside {
  display: flex;
  flex-direction: column;
  align-items: start;
  justify-content: start;

  gap: 12px;

  ul {
    margin: 0;
    padding: 0;
    list-style: none;
    li {
      font-size: 15px;

      &:before {
        content: '-';
        margin-right: 1ch;
        margin-left: 4px;
        color: black !important;
      }
    }
  }
}
.ux {
  &-clickable {
    color: royalblue;
    &:hover {
      cursor: pointer;
      color: orange;
    }
  }
}
</style>
