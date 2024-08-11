<template>
  <div uk-grid class="uk-height-1-1 uk-margin-remove uk-padding-remove">
    <div class="control-component">
      <InstrumentControlPanel />
    </div>
    <div class="view-component uk-width-expand">
      <StreamControl />
    </div>
  </div>
</template>

<script>
import InstrumentControlPanel from './instrumentControlPanel.vue';
import StreamControl from '../streamControl/streamControl.vue';
export default {
  name: "Components Control",

  components: {
    InstrumentControlPanel,
    StreamControl
  }
}
</script>