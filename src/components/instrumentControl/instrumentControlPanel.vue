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
            <div>
              <!-- Exposure time -->
              <div class="uk-margin-small uk-margin-remove-bottom">
                <label class="uk-form-label" for="form-stacked-text">
                  Exposure time (ms)
                </label>
                <div class="uk-margin-remove-bottom" uk-grid>
                  <div class="uk-width-2-3">
                    <input
                      v-model="cameraExposureTime"
                      class="uk-input uk-form-small"
                      type="number"
                      min="1000"
                      @keyup.enter="handlePutExposureTime"
                    />
                  </div>
                  <div class="uk-width-1-3">
                    <button
                      class="uk-button uk-form-small uk-button-primary uk-margin-small uk-margin-remove-top uk-width-1-1"
                      @click="handlePutExposureTime()"
                    >
                      Set
                    </button>
                  </div>
                </div>
              </div>
              <!-- Pixel format -->
              <div class="uk-margin-small uk-margin-remove-bottom">
                <label class="uk-form-label" for="form-stacked-text">
                  Pixel format
                </label>
                <div class="uk-margin-remove-bottom" uk-grid>
                  <div class="uk-width-2-3">
                    <!-- <input
                      v-model="cameraPixelFormat"
                      class="uk-input uk-form-small"
                      type="text"
                      min="100"
                    /> -->
                    <select v-model="cameraPixelFormat" class="uk-select uk-form-small uk-margin-small" @change="onSetPixelFormat($event)">
                <option>MONO8</option>
                <option>MONO10</option>
                <option>MONO12</option>
              </select>   
                              </div>
                  <div class="uk-width-1-3">
                    <button
                      class="uk-button uk-form-small uk-button-primary uk-margin-small uk-margin-remove-top uk-width-1-1"
                      @click="handlePutPixelFormat()"
                    >
                      Set
                    </button>
                  </div>                
                </div>
              </div>
              <div class="uk-margin-small uk-margin-remove-bottom">
                <button
                  class="uk-button uk-form-small uk-button-primary uk-margin-small uk-margin-remove-top uk-width-1-1"
                  @click="handleOpenCamera()"
                >
                  Open Camera
                </button>
              </div>
              <div class="uk-margin-small uk-margin-remove-bottom uk-margin-remove-top">
                <button
                  class="uk-button uk-form-small uk-button-primary uk-margin-small uk-margin-remove-top uk-width-1-1"
                  @click="handleStartStreaming()"
                >
                  Start Streaming
                </button>
              </div>
              <div class="uk-margin-small uk-margin-remove-bottom uk-margin-remove-top">
                <button
                  class="uk-button uk-form-small uk-button-primary uk-margin-small uk-margin-remove-top uk-width-1-1"
                  @click="handleStopStreaming()"
                >
                  Stop Streaming
                </button>
              </div>
              <div class="uk-margin-small uk-margin-remove-bottom uk-margin-remove-top">
                <button
                  class="uk-button uk-form-small uk-button-primary uk-margin-small uk-margin-remove-top uk-width-1-1"
                  @click="handleCloseCamera()"
                >
                  Close Camera
                </button>
              </div>
              <div class="uk-margin-small uk-margin-remove-bottom uk-margin-remove-top">
                <button
                  class="uk-button uk-form-small uk-button-primary uk-margin-small uk-margin-remove-top uk-width-1-1"
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
          <div>
            <div class="uk-margin-small uk-margin-remove-bottom">
              <label class="uk-form-label" for="form-stacked-text">
                Color Filter:
              </label>
              <select v-model="colorFilter" class="uk-select uk-form-small uk-margin-small" @change="onSetColorFilter($event)">
                <option>X</option>
                <option>Y</option>
                <option>Z</option>
                <option>CLEAR</option>
              </select>            


              <div class="uk-margin-small uk-margin-remove-bottom uk-margin-remove-top">
                <button
                  class="uk-button uk-form-small uk-button-primary uk-margin-small uk-margin-remove-top uk-width-1-1"
                  @click="handleGetColorFilter()"
                >
                  Get Color Filter
                </button>
              </div>
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
              <select v-model="ndFilter" class="uk-select uk-form-small uk-margin-small" @change="onSetNDFilter($event)">
                <option>CLEAR</option>
                <option>ND1</option>
                <option>ND2</option>
                <option>ND3</option>
                <option>BLOCK</option>
              </select>            
            </div>
            <div class="uk-margin-small uk-margin-remove-bottom uk-margin-remove-top">
                <button
                  class="uk-button uk-form-small uk-button-primary uk-margin uk-margin-remove-top uk-width-1-1"
                  @click="handleGetNDFilter()"
                >
                  Get ND Filter
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
            <div class="uk-margin-small uk-margin-remove-bottom ">
              <button
                class="uk-button uk-form-small uk-button-primary uk-margin-small uk-margin-remove-top uk-width-1-1"
                @click="handleGetStagePosition()"
              >
                Get Stage Position
              </button>
            </div>
            <div 
              class="uk-margin-small uk-margin-remove-bottom uk-margin-remove-top" 
              uk-grid
            >
              <div class="uk-width-1-4 uk-margin-small uk-margin-remove-top">
                <button
                  class="uk-button uk-form-small uk-button-primary uk-margin-small uk-margin-remove-top uk-margin-remove-bottom uk-width-1-1"
                  @click="handleMoveStagePositionRel(-0.1)"
                >
                  -0.1
                </button>
              </div>
              <div class="uk-width-expand uk-margin-remove-top">
                <button
                  class="uk-button uk-form-small uk-button-primary uk-margin-small uk-margin-remove-top uk-margin-remove-bottom uk-width-1-1"
                  @click="handleMoveStagePositionAbs()"
                >
                  Move Abs
                </button>
              </div>
              <div class="uk-width-1-4 uk-margin-small uk-margin-remove-top">
                <button
                  class="uk-button uk-form-small uk-button-primary uk-margin-small uk-margin-remove-top uk-margin-remove-bottom uk-width-1-1"
                  @click="handleMoveStagePositionRel(0.1)"
                >
                  +0.1
                </button>
              </div>
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
            <!-- RX Spherical Power -->
            <div class="uk-margin-small uk-margin-remove-bottom">
              <label class="uk-form-label" for="form-stacked-text">
                Spherical power:
              </label>
              <input
                v-model="prescriptionSphericalPower"
                class="uk-input uk-form-small"
                type="number"
              />
            </div>
            <div class="uk-margin-small uk-margin-remove-bottom">
              <button
                class="uk-button uk-form-small uk-button-primary uk-margin-small uk-margin-remove-top uk-margin-remove-bottom uk-width-1-1"
                @click="handleGetRxSphPower()"
              >
                Get Sph Power
              </button>
            </div>
            <div class="uk-margin-small uk-margin-remove-bottom">
              <button
                class="uk-button uk-form-small uk-button-primary uk-margin-small uk-margin-remove-top uk-margin-remove-bottom uk-width-1-1"
                @click="handleMoveRxSphPower()"
              >
                Move Sph Power
              </button>
            </div>

            <!-- RX Cylindrical Power -->
            <div class="uk-margin-small uk-margin-remove-bottom">
              <label class="uk-form-label" for="form-stacked-text">
                Cylindrical power:
              </label>
              <input
                v-model="prescriptionCylindricalPower"
                class="uk-input uk-form-small"
                type="number"
              />
            </div>
            <div class="uk-margin-small uk-margin-remove-bottom">
              <button
                class="uk-button uk-form-small uk-button-primary uk-margin-small uk-margin-remove-top uk-margin-remove-bottom uk-width-1-1"
                @click="handleGetRxCylPower()"
              >
                Get Cyl Power
              </button>
            </div>
            <div class="uk-margin-small uk-margin-remove-bottom">
              <button
                class="uk-button uk-form-small uk-button-primary uk-margin-small uk-margin-remove-top uk-margin-remove-bottom uk-width-1-1"
                @click="handleMoveRxCylPower()"
              >
                Move Cyl Power
              </button>
            </div>

            <!-- RX Cylindrical axis -->
            <div class="uk-margin-small uk-margin-remove-bottom">
              <label class="uk-form-label" for="form-stacked-text">
                Cylindrical axis:
              </label>
              <input
                v-model="prescriptionCylindricalAxis"
                class="uk-input uk-form-small"
                type="number"
              />
            </div>
            <div class="uk-margin-small uk-margin-remove-bottom">
              <button
                class="uk-button uk-form-small uk-button-primary uk-margin-small uk-margin-remove-top uk-margin-remove-bottom uk-width-1-1"
                @click="handleGetRxCylAxis()"
              >
                Get Cyl Axis
              </button>
            </div>
            <div class="uk-margin-small uk-margin-remove-bottom">
              <button
                class="uk-button uk-form-small uk-button-primary uk-margin-small uk-margin-remove-top uk-margin-remove-bottom uk-width-1-1"
                @click="handleMoveRxCylAxis()"
              >
                Move Cyl Axis
              </button>
            </div>
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: "Components-Control-Panel",

  data: function() {
    return {
      filename: "",
      temporary: false,
      fullResolution: false,
      storeBayer: false,
      resizeCapture: false,
      captureNotes: "",
      resizeDims: [640, 480],
      cameraPixelFormat: "Mono8",
      cameraExposureTime: 30,
      colorFilter: 'X',
      ndFilter: 'ND1',
      focusingPosition: 12.345,
      aperature: '3mm',
      prescriptionSphericalPower: 0.0,
      prescriptionCylindricalPower: 0.0,
      prescriptionCylindricalAxis: 0.0
    }
  },

  computed: {
    resizeClass: function() {
      return {
        "uk-disabled": !this.resizeCapture
      }
    }
  },

  mounted: function() {
    this.handleGetExposureTime()
    this.handleGetPixelFormat()
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
    handleGetExposureTime: function() {
      axios.get("http://localhost:8000/myxthing/exposure_time").then(response => {
        var exposure = response.data
        this.cameraExposureTime = exposure 
      })
    },
    handlePutExposureTime: function() {
      const config = { headers: {'Content-Type': 'application/json'} };
      axios.put("http://localhost:8000/myxthing/exposure_time", this.cameraExposureTime, config)
    },
    handleGetPixelFormat: function() {
      axios.get("http://localhost:8000/myxthing/pixel_format").then(response => {
        var format = response.data
        this.cameraPixelFormat = format
      })
    },
    handlePutPixelFormat: function() {
      const config = { headers: {'Content-Type': 'application/json'} };
      axios.put("http://localhost:8000/myxthing/pixel_format", this.cameraPixelFormat, config)
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
    onSetColorFilter: function(event) {
      this.handlePostColorFilter()
    },
    onSetPixelFormat: function(event) {
      this.handlePutPixelFormat()
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
    onSetNDFilter: function(event) {
      console.log(event)
      this.handlePostNDFilter()
    },
    handleGetStagePosition: function() {
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
    },

    handleGetRxSphPower: function() {
      axios.get("http://localhost:8000/myxthing/rx_sph_power").then(response => {
        this.prescriptionSphericalPower = response.data
      })
    },
    handleMoveRxSphPower: function() {
      const config = { headers: {'Content-Type': 'application/json'} };
      axios.post("http://localhost:8000/myxthing/move_rx_sph_power", this.prescriptionSphericalPower, config).then(() => {
        this.handleGetRxSphPower()
      })
    },

    handleGetRxCylPower: function() {
      axios.get("http://localhost:8000/myxthing/rx_cyl_power").then(response => {
        this.prescriptionCylindricalPower = response.data
      })
    },
    handleMoveRxCylPower: function() {
      const config = { headers: {'Content-Type': 'application/json'} };
      axios.post("http://localhost:8000/myxthing/move_rx_cyl_power", this.prescriptionCylindricalPower, config).then(() => {
        this.handleGetRxCylPower()
      })
    },

    handleGetRxCylAxis: function() {
      axios.get("http://localhost:8000/myxthing/rx_cyl_axis").then(response => {
        this.prescriptionCylindricalAxis = response.data
      })
    },
    handleMoveRxCylAxis: function() {
      const config = { headers: {'Content-Type': 'application/json'} };
      axios.post("http://localhost:8000/myxthing/move_rx_cyl_axis", this.prescriptionCylindricalAxis, config).then(() => {
        this.handleGetRxCylAxis()
      })
    }
  }
}
</script>