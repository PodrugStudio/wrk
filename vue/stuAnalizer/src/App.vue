<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
// import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <header>
    <RouterLink to="/">Dashboard</RouterLink>
    <RouterLink to="/admin">Admin</RouterLink>
    <RouterLink to="/homes">Homes</RouterLink>
    <!-- <RouterLink to="/">Analiza</RouterLink>
    <RouterLink to="/Homes">Homes</RouterLink> -->
  </header>
  <RouterView />
</template>
