<template>
  <div
    id="stream-display"
    ref="streamDisplay"
    class="stream-display uk-width-1-1 uk-height-1-1 scrollTarget"
  >
    <img
      ref="click-frame"
      class="uk-align-center uk-margin-remove-bottom"
      :src="streamImgUri"
      alt="Stream"
    />
  </div>
</template>

<script>
export default {
  name: "MiniStreamDisplay",

  computed: {
    streamImgUri: function() {
      return "http://localhost:8000/myxthing/png_stream_cv"
    }
  }
}
</script>

<style scoped lang="less">
.stream-display img {
  text-align: center;
  object-fit: contain;
  border: 1px solid #555;
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
