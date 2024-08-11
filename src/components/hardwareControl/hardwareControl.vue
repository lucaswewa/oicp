<template>
  <div uk-grid class="uk-height-1-1 uk-margin-remove uk-padding-remove">
    <div class="control-component">
      <HardwareControlPanel/>
    </div>
  </div>
</template>

<script>
import HardwareControlPanel from './hardwareControlPanel.vue';

export default {
  name: "Components Control",

  components: {
    HardwareControlPanel
  }
}
</script>