<template>
  <div
    id="stage-control-panel"
    class="uk-padding-small"
  >
    <ul uk-accordion="multiple: true">
      <!-- Config section -->
      <li>
        <a class="uk-accordion-title" href="#">Configure</a>
        <div class="uk-accordion-content">
          <p>Step Size</p>
          <div class="uk-grid-small uk-child-width-1-3" uk-grid>
            <div>
              <label class="uk-form-label" for="form-stacked-text">x</label>
              <div class="uk-form-controls">
                <input v-model="stepSize.x" class="uk-input uk-form-small" type="number" name="inputStepX"/>
              </div>
              <label class="uk-margin-small-right">
                <input v-model="invert.x" class="uk-checkbox" type="checkbox"/>Invert x
              </label>
            </div>

            <div>
              <label class="uk-form-label" for="form-stacked-text">y</label>
              <div class="uk-form-controls">
                <input v-model="stepSize.y" class="uk-input uk-form-small" type="number" name="inputStepY"/>
              </div>
              <label class="uk-margin-small-right">
                <input v-model="invert.y" class="uk-checkbox" type="checkbox"/>Invert y
              </label>
            </div>

            <div>
              <label class="uk-form-label" for="form-stacked-text">z</label>
              <div class="uk-form-controls">
                <input v-model="stepSize.z" class="uk-input uk-form-small" type="number" name="inputStepZ"/>
              </div>
              <label class="uk-margin-small-right">
                <input v-model="invert.z" class="uk-checkbox" type="checkbox"/>Invert z
              </label>
            </div>
          </div>

          <button class="uk-button uk-button-default uk-margin uk-width-1-1" @click="homeStage()">Home Stage</button>
        </div>
      </li>

      <!-- Move-to section -->
      <li class="uk-open">
        <a class="uk-accordion-title" href="#">Move to</a>
        <div class="uk-accordion-content">
          <form @submit.prevent="handleSubmit">
            <div class="uk-grid-small uk-child-width-1-3" uk-grid>
              <div>
                <label class="uk-form-label" for="form-stacked-text">x</label>
                <div class="uk-form-controls">
                  <input v-model="setPosition.x" class="uk-input uk-form-small" type="number" name="inputPositionX"/>
                </div>
              </div>

              <div>
                <label class="uk-form-label" for="form-stacked-text">y</label>
                <div class="uk-form-controls">
                  <input v-model="setPosition.y" class="uk-input uk-form-small" type="number" name="inputPositionX"/>
                </div>
              </div>

              <div>
                <label class="uk-form-label" for="form-stacked-text">z</label>
                <div class="uk-form-controls">
                  <input v-model="setPosition.z" class="uk-input uk-form-small" type="number" name="inputPositionX"/>
                </div>
              </div>
            </div>

            <p>
              <button type="submit" class="uk-button uk-button-default uk-float-right uk-width-1-1">Move</button>
            </p>
          </form>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "Stage Control Panel",

  data: function() {
    return {
      range: {
        x: {
          max: 10,
          min: 0
        },
        y: {
          max: 10,
          min: 0
        },
        z: {
          max: 10,
          min: 0
        }
      },
      stepSize: {
        x: 10,
        y: 10,
        z: 10
      },
      invert: {
        x: false,
        y: false,
        z: false
      },
      setPosition: {
        x: 0,
        y: 0,
        z: 0
      }
    }
  }
}
</script>