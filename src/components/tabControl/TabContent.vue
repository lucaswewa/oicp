<template>
  <div
    :hidden="currentTab != tabID"
    class="uk-width-expand uk-height-1-1"
  >
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: "TabContent",

  props: {
    tabID: {
      type: String,
      required: true
    },
    currentTab: {
      type: String,
      required: true
    }
  }
}
</script>

<style scoped>

</style>
