<template>
  <div
    id="capture-control-panel"
    class="uk-padding-small">

    <ul uk-accordion="multiple: true">
      <!-- Camera Control -->
      <li :class="{ 'uk-open': true }">
          <a class="uk-accordion-title" href="#">Camera Control</a>
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
              <div class="uk-margin-small uk-margin-remove-bottom">
                <button
                  class="uk-button uk-button-primary uk-margin uk-margin-remove-top uk-width-1-1"
                  @click="handleOpenCamera()"
                >
                  Open Camera
                </button>
              </div>
              <div class="uk-margin-small uk-margin-remove-bottom">
                <button
                  class="uk-button uk-button-primary uk-margin uk-margin-remove-top uk-width-1-1"
                  @click="handleCloseCamera()"
                >
                  Close Camera
                </button>
              </div>
              <div class="uk-margin-small uk-margin-remove-bottom">
                <button
                  class="uk-button uk-button-primary uk-margin uk-margin-remove-top uk-width-1-1"
                  @click="handleStartStreaming()"
                >
                  Start Streaming
                </button>
              </div>
              <div class="uk-margin-small uk-margin-remove-bottom">
                <button
                  class="uk-button uk-button-primary uk-margin uk-margin-remove-top uk-width-1-1"
                  @click="handleStopStreaming()"
                >
                  Stop Streaming
                </button>
              </div>
              <div class="uk-margin-small uk-margin-remove-bottom">
                <button
                  class="uk-button uk-button-primary uk-margin uk-margin-remove-top uk-width-1-1"
                  @click="handleCapture()"
                >
                  Capture
                </button>
              </div>
            </div>
          </div>
      </li> 

      <!-- Color Filters Control -->
      <li :class="{ 'uk-open': true }">
        <a class="uk-accordion-title" href="#">Color Filters Control</a>
        <div class="uk-accordion-content">
          <div >
            <div class="uk-margin-small uk-margin-remove-bottom">
              <label class="uk-form-label" for="form-stacked-text">
                Color Filter:
              </label>
              <input
                v-model="colorFilter"
                class="uk-input uk-form-small"
                type="string"
              />
            </div>
            <div class="uk-margin-small uk-margin-remove-bottom">
                <button
                  class="uk-button uk-button-primary uk-margin uk-margin-remove-top uk-width-1-1"
                  @click="handleGetColorFilter()"
                >
                  Get Color Filter
                </button>
              </div>
              <div class="uk-margin-small uk-margin-remove-bottom">
                <button
                  class="uk-button uk-button-primary uk-margin uk-margin-remove-top uk-width-1-1"
                  @click="handlePostColorFilter()"
                >
                  Change Color Filter
                </button>
              </div>
          </div>
        </div>
      </li>

      <!-- ND Filters Control -->
      <li :class="{ 'uk-open': true }">
        <a class="uk-accordion-title" href="#">ND Filters Control</a>
        <div class="uk-accordion-content">
          <div >
            <div class="uk-margin-small uk-margin-remove-bottom">
              <label class="uk-form-label" for="form-stacked-text">
                ND Filter:
              </label>
              <input
                v-model="ndFilter"
                class="uk-input uk-form-small"
                type="string"
              />
            </div>
            <div class="uk-margin-small uk-margin-remove-bottom">
                <button
                  class="uk-button uk-button-primary uk-margin uk-margin-remove-top uk-width-1-1"
                  @click="handleGetNDFilter()"
                >
                  Get ND Filter
                </button>
              </div>
              <div class="uk-margin-small uk-margin-remove-bottom">
                <button
                  class="uk-button uk-button-primary uk-margin uk-margin-remove-top uk-width-1-1"
                  @click="handlePostNDFilter()"
                >
                  Change ND Filter
                </button>
              </div>
          </div>
        </div>
      </li>

      <!-- Focusing Control -->
      <li :class="{ 'uk-open': true }">
        <a class="uk-accordion-title" href="#">Focusing Control</a>
        <div class="uk-accordion-content">
          <div >
            <div class="uk-margin-small uk-margin-remove-bottom">
              <label class="uk-form-label" for="form-stacked-text">
                Focusing motor position:
              </label>
              <input
                v-model="focusingPosition"
                class="uk-input uk-form-small"
                type="number"
              />
            </div>
            <div class="uk-margin-small uk-margin-remove-bottom">
              <button
                class="uk-button uk-button-primary uk-margin uk-margin-remove-top uk-width-1-1"
                @click="handleGetStagePosition()"
              >
                Get Stage Position
              </button>
            </div>
            <div class="uk-margin-small uk-margin-remove-bottom">
              <button
                class="uk-button uk-button-primary uk-margin uk-margin-remove-top uk-width-1-1"
                @click="handleMoveStagePositionAbs()"
              >
                Move to Position
              </button>
            </div>
            <div 
              class="uk-child-width-1-2"
              uk-grid
            >
              <p>
                <button
                  class="uk-button uk-button-primary uk-margin uk-margin-remove-top uk-width-1-1"
                  @click="handleMoveStagePositionRel(-0.5)"
                >
                  Move Near -0.5 mm
                </button>
              </p>
              <p>
                <button
                  class="uk-button uk-button-primary uk-margin uk-margin-remove-top uk-width-1-1"
                  @click="handleMoveStagePositionRel(0.5)"
                >
                  Move Far +0.5 mm
                </button>
              </p>
            </div>
          </div>
        </div>
      </li>

      <!-- Aperture Control -->
      <li :class="{ 'uk-open': false }">
        <a class="uk-accordion-title" href="#">Aperture Control</a>
        <div class="uk-accordion-content">
          <div >
            <div class="uk-margin-small uk-margin-remove-bottom">
              <label class="uk-form-label" for="form-stacked-text">
                Aperture size:
              </label>
              <input
                v-model="aperature"
                class="uk-input uk-form-small"
                type="string"
              />
            </div>
          </div>
        </div>
      </li>

      <!-- Prescription Compensation Control -->
      <li :class="{ 'uk-open': false }">
        <a class="uk-accordion-title" href="#">Prescription Compensation Control</a>
        <div class="uk-accordion-content">
          <div >
            <div class="uk-margin-small uk-margin-remove-bottom">
              <label class="uk-form-label" for="form-stacked-text">
                Spherical power:
              </label>
              <input
                v-model="prescriptionSphericalPower"
                class="uk-input uk-form-small"
                type="string"
              />
            </div>
            <div class="uk-margin-small uk-margin-remove-bottom">
              <label class="uk-form-label" for="form-stacked-text">
                Cylindrical power:
              </label>
              <input
                v-model="prescriptionCylindricalPower"
                class="uk-input uk-form-small"
                type="string"
              />
            </div>
            <div class="uk-margin-small uk-margin-remove-bottom">
              <label class="uk-form-label" for="form-stacked-text">
                Cylindrical axis:
              </label>
              <input
                v-model="prescriptionCylindricalAxis"
                class="uk-input uk-form-small"
                type="string"
              />
            </div>
            <div class="uk-margin-small uk-margin-remove-bottom">
              <button
                class="uk-button uk-button-primary uk-margin uk-margin-remove-top uk-width-1-1"
                @click="handleFocusing()"
              >
                Apply Prescription Compensation
              </button>
            </div>
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import axios
 from 'axios';
export default {
  name: "Components Control Panel",

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
      colorFilter: 'X',
      ndFilter: 'ND1',
      focusingPosition: 12.345,
      aperature: '3mm',
      prescriptionSphericalPower: '-1d',
      prescriptionCylindricalPower: '-1d',
      prescriptionCylindricalAxis: '15deg'
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
      axios.post("http://localhost:8000/myxthing/capture_camera")
    },
    handleOpenCamera: function() {
      console.log("handle Open Camera")
      axios.post("http://localhost:8000/myxthing/open_camera")
    },
    handleCloseCamera: function() {
      console.log("handle Close Camera")
      axios.post("http://localhost:8000/myxthing/close_camera")
    },
    handleStartStreaming: function() {
      console.log("handle Start Streaming")
      axios.post("http://localhost:8000/myxthing/start_stream_camera")
    },
    handleStopStreaming: function() {
      console.log("handle Stop Streaming")
      axios.post("http://localhost:8000/myxthing/stop_stream_camera")
    },
    handleGetColorFilter: function() {
      console.log(this.colorFilter)
      axios.get("http://localhost:8000/myxthing/color_filter").then(response => {
        console.log(response.data)
        this.colorFilter = response.data
      })
    },
    handlePostColorFilter: function() {
      console.log(this.colorFilter)
      const config = { headers: {'Content-Type': 'application/json'} };
      axios.post("http://localhost:8000/myxthing/move_color_filter", this.colorFilter, config)
    },
    handleGetNDFilter: function() {
      console.log(this.ndFilter)
      axios.get("http://localhost:8000/myxthing/nd_filter").then(response => {
        console.log(response.data)
        this.ndFilter = response.data
      })
    },
    handlePostNDFilter: function() {
      console.log(this.ndFilter)
      const config = { headers: {'Content-Type': 'application/json'} };
      axios.post("http://localhost:8000/myxthing/move_nd_filter", this.ndFilter, config)
    },
    handleGetStagePosition: function() {
      const config = { headers: {'Content-Type': 'application/json'} };
      axios.get("http://localhost:8000/myxthing/stage").then(response => {
        this.focusingPosition = response.data
      })
    },
    handleMoveStagePositionAbs: function() {
      const config = { headers: {'Content-Type': 'application/json'} };
      axios.post("http://localhost:8000/myxthing/move_stage_abs", this.focusingPosition, config).then(() => {
        this.handleGetStagePosition()
      })
    },
    handleMoveStagePositionRel: function(pos_rel) {
      const config = { headers: {'Content-Type': 'application/json'} };
      axios.post("http://localhost:8000/myxthing/move_stage_rel", pos_rel, config).then(() => {
        this.handleGetStagePosition()
      })
    }
  }
}
</script>