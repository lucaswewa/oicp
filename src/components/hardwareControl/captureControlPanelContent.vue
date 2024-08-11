<template>
  <div
    id="capture-control-panel"
    class="uk-padding-small">
    <div>
      <label class="uk-form-label" for="form-stacked-text">Filename</label>
      <input
        v-model="filename"
        class="uk-input uk-width-1-1 uk-form-small"
        name="inputFilename"
        placeholder="Leave blank for default"
      />
    </div>

    <p>
      <label>
        <input v-model="temporary" class="uk-checkbox" type="checkbox" />
        Temporary
      </label
      >
    </p>

    <hr />

    <div 
      class="uk-child-width-1-2"
      uk-grid
    >
      <p>
        <label>
          <input
            v-model="fullResolution"
            class="uk-checkbox"
            type="checkbox"
          />
          Full resolution
        </label>
      </p>
      <p>
        <label>
          <input v-model="storeBayer" class="uk-checkbox" type="checkbox" />
          Store raw data
        </label>
      </p>
    </div>

    <hr />

    <p>
      <label>
        <input v-model="resizeCapture" class="uk-checkbox" type="checkbox" />
        Resize capture
      </label>
    </p>

    <div class="uk-child-width-1-2" uk-grid>
      <div>
        <input
          v-model="resizeDims[0]"
          :class="resizeClass"
          class="uk-input uk-form-width-medium uk-form-small"
          type="number"
          name="inputResizeW"
        />
      </div>
      <div>
        <input
          v-model="resizeDims[1]"
          :class="resizeClass"
          class="uk-input uk-form-width-medium uk-form-small"
          type="number"
          name="inputResizeH"
        />
      </div>
    </div>

    <ul uk-accordion="multiple: true">
      <li>
        <a class="uk-accordion-title" href="#">Notes</a>
        <div class="uk-accordion-content">
          <div class="uk-margin-small">
            <textarea
              v-model="captureNotes"
              class="uk-textarea"
              rows="5"
              placeholder="Capture notes"
            ></textarea>
          </div>
        </div>
      </li>
    </ul>

    <hr />

    <ul uk-accordion="multiple: true">
      <li :class="{ 'uk-open': true }">
        <a class="uk-accordion-title" href="#">Camera settings</a>
        <div
          class="uk-accordion-content"
        >
          <div class="uk-margin">
            <label>
              <input
                v-model="cameraSettingsEnabled"
                class="uk-checkbox"
                type="checkbox"
              />
              Enable camera settings
            </label>
          </div>
          <p>
            If `Enable camera settings` is checked, you can make changes to the
            camera.
          </p>
          <div>
            <div class="uk-margin-small uk-margin-remove-bottom">
              <label class="uk-form-label" for="form-stacked-text">
                Exposure time (ms)
              </label>
              <input
                v-model="cameraExposureTime"
                class="uk-input uk-form-small"
                type="number"
                min="1000"
              />
            </div>
            <div class="uk-margin-small uk-margin-remove-bottom">
              <label class="uk-form-label" for="form-stacked-text">
                Pixel format
              </label>
              <input
                v-model="cameraPixelFormat"
                class="uk-input uk-form-small"
                type="text"
                min="100"
              />
            </div>
          </div>
        </div>
      </li>
    </ul>

    <button
      class="uk-button uk-button-primary uk-margin uk-margin-remove-top uk-width-1-1"
      @click="handleCapture()"
    >
      Capture
    </button>
  </div>
</template>

<script>
export default {
  name: "Capture Control Panel",

  data: function() {
    return {
      filename: "",
      temporary: false,
      fullResolution: false,
      storeBayer: false,
      resizeCapture: false,
      captureNotes: "",
      resizeDims: [640, 480],
      cameraSettingsEnabled: false,
      cameraPixelFormat: "Mono8",
      cameraExposureTime: 30,   

    }
  },

  computed: {
    resizeClass: function() {
      return {
        "uk-disabled": !this.resizeCapture
      }
    }
  },

  methods: {
    handleCapture: function() {
      console.log("handle capture")
    }
  }
}
</script>