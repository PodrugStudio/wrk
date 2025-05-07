<script setup lang="ts">
import { computed, ref } from 'vue'
import { includes, filter, orderBy } from 'lodash-es'
import { homes, type HOME } from '@/code/users'

const fValue = ref('')
const filteredHomes = computed(() =>
  filter(homes, function (h: HOME) {
    return includes(h.dir, fValue.value)
  })
)
</script>
<template>
  <aside>
    <blockquote>List all homes and check if user exists in valid users</blockquote>
    <input v-model="fValue" type="text" placeholder="Search" />
    <br />
    fValue: {{ fValue }}
    <hr />
    <h5>Oni weird</h5>
    <ul>
      <li>jelena.antunovic.simic</li>
      <li>andreja.arbanas.vrban1</li>
      <li>james.nkemakonam.atuorah2</li>
      <li>katarina.lidija.garic</li>
      <li>srecka.juranovic.petrov2</li>
      <li>hema.kristina.ontl1</li>
      <li>ivis.yarelis.st.rose.miro</li>
      <li>issydora.rossanda.tesic1</li>
      <li>mirela.vickovic.batistic1</li>
      <li>prerana.yonjan.tamang2</li>
      <li>marija.zupcic.rogic1</li>
    </ul>
  </aside>
  <main>
    <table>
      <tr>
        <th>idx</th>
        <!-- <th>ID</th> -->
        <!-- <th>uName</th> -->
        <th>📪</th>
        <th>hasUser</th>
        <th>radnik</th>
        <!-- <th>safe to delete</th> -->
      </tr>
      <tr v-for="(home, idx) in orderBy(filteredHomes, 'hasUser')" :key="`h${idx}`">
        <td>{{ idx + 1 }}</td>
        <td>{{ home.dir }}</td>
        <td>{{ home.hasUser }}</td>
        <td>{{ home.radnik?.id }}</td>
        <!-- <td></td> -->
      </tr>
    </table>
  </main>
</template>

<style>
table {
  width: 100%;
}
</style>
