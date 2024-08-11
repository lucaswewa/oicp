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
                @click="handleFocusing()"
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
                  @click="handleFocusing()"
                >
                  Move Near
                </button>
              </p>
              <p>
                <button
                  class="uk-button uk-button-primary uk-margin uk-margin-remove-top uk-width-1-1"
                  @click="handleFocusing()"
                >
                  Move Far
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
    }
  }
}
</script>