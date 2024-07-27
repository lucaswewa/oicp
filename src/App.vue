<template>
  <div
    id="app-content-container"
    class="uk-height-1-1 uk-margin-remove uk-padding-remove"
  >
    <AppContent/>
  </div>
</template>

<script>
import AppContent from './components/AppContent.vue';

export default {
  name: "OicpApp",
  data: function() {
    return {
      name: "My OICP App"
    }
  },
  components: {
    AppContent
  }
}
</script>


<style lang="less">
@import "../node_modules/uikit/src/less/uikit.less";
@import "./assets/less/theme.less";
</style>
