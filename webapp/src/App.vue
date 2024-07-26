<template>
  <div id="app-content-container">
    <AppContent/>
  </div>
</template>

<script>
import AppContent from './components/AppContent.vue';

export default {
  name: "App",
  data: function() {
    return {
      name: "my name"
    }
  },
  components: {
    AppContent
  }
}
</script>