<template>
  <div uk-grid class="uk-height-1-1 uk-margin-remove uk-padding-remove">
    <div class="control-component">
      <InstrumentControlPanel />
    </div>
    <div class="view-component uk-width-expand">
      <MiniStreamControl />
    </div>
  </div>
</template>

<script setup>
import InstrumentControlPanel from './instrumentControlPanel.vue';
import StreamControl from '../streamControl/streamControl.vue';
import MiniStreamControl from '../streamControl/miniStreamControl.vue';
</script>