<template>
  <div uk-grid class="uk-height-1-1 uk-margin-remove uk-padding-remove">
    <div class="control-component">
      <CaptureControlPanelContent/>
    </div>
  </div>
</template>

<script>
import CaptureControlPanelContent from './captureControlPanelContent.vue';
import captureControlPanelContent from './captureControlPanelContent.vue';

export default {
  name: "Capture Content",

  components: {
    CaptureControlPanelContent
  }
}
</script>