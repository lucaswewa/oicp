<template>
  <div uk-grid class="uk-height-1-1 uk-margin-remove uk-padding-remove">
    <div class="control-component">
      <StageControlPanelContent/>
    </div>
  </div>
</template>

<script>
import StageControlPanelContent from './StageControlPanelContent.vue';

export default {
  name: "Stage Content",

  components: {
    StageControlPanelContent
  }
}
</script>