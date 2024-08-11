<template>
  <div
    id="stream-display"
    ref="streamDisplay"
    class="stream-display uk-width-1-1 uk-height-1-1 scrollTarget"
  >
    <img
      ref="click-frame"
      class="uk-align-center uk-margin-remove-botton"
      :src="streamImgUri"
      alt="Stream"
      @dblclick="clickMonitor"
    />
  </div>
</template>

<script>
export default {
  name: "StreamDisplay",
  computed: {
    streamImgUri: function() {
      return "http://localhost:8000/myxthing/png_stream_cv"
    }
  }
}
</script>

<style scoped lang="less">
.stream-display img {
  height: 100%;
  text-align: center;
  object-fit: contain;
}

.stream-display {
  width: 100%;
  height: 100%;
}

.position-relative {
  position: relative !important;
}

.text-center {
  text-align: center;
}
</style>