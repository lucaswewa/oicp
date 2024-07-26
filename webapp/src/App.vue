<template>
  <div id="oicp_app">
    <OicpAppContent/>
  </div>
</template>

<script>
import OicpAppContent from './components/AppContent.vue';

export default {
  name: "App",
  data: function() {
    return {
      name: "my name"
    }
  },
  components: {
    OicpAppContent
  }
}
</script>