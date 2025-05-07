<template>
  <div>Dashboard</div>
</template>

<script setup lang="ts">
import axios from 'axios'
import { Buffer } from 'buffer'

const username = 'user'
const password = 'pass'

// Encode username and password in base64
const encoded = Buffer.from(username + ':' + password).toString('base64')

axios
  .get('http://placa.studenac.hr/app/api', {
    headers: {
      Authorization: 'Basic ' + encoded
    }
  })
  .then((response) => {
    console.log(response.data)
  })
  .catch((error) => {
    console.error('There was an error!', error)
  })
</script>
