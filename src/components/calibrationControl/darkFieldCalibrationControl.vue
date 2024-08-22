<template>
  <div
    id="dark-control-panel"
    class="uk-padding-small"
  >
    <ul uk-accordion="multiple: true">
      <li :class="{ 'uk-open': true }">
        <a class="uk-accordion-title" href="#">Dark Field Calibration Detail</a>
        <p>[name], [display name]</p>
        <p>description</p>
        <p>binning_x</p>
        <p>binning_y</p>
        <p>image_width</p>
        <p>image_height</p>
        <p>image_data view</p>
        <p>[ROI location], [ROI size], [ROI shape]</p>
        <p>chart</p>
        <p>[take image], [load image], [save], [delete], [next], [prev], [last], [first]</p>
      </li>
      <li :class="{ 'uk-open': true }">
        <a class="uk-accordion-title" href="#">Dark Field Calibration List (6)</a>
        <div class="uk-accordion-content">
          <div>
            <div class="uk-overflow-auto">
              <table class="uk-table uk-table-hover uk-table-middle uk-table-divider">
                <thead>
                  <tr>
                    <th class="uk-table-shrink"></th>
                    <th class="uk-table-shrink">Preserve</th>
                    <th class="uk-table-expand">Expand + Link</th>
                    <th class="uk-width-small">Truncate</th>
                    <th class="uk-table-shrink uk-text-nowrap">Shrink + Nowrap</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><input class="uk-checkbox" type="checkbox" aria-label="Checkbox"></td>
                    <td>
                      <img class="uk-preserve-width uk-border-circle" src="../asserts/dark_field_cali.png" width="40" height="40" alt="">
                    </td>
                    <td class="uk-table-link">
                      <a class="uk-link-reset" href="#" @click="clickMe">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.</a>
                    </td>
                    <td class="uk-text-truncate">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.</td>
                    <td class="uk-text-nowrap">Lorem ipsum dolor</td>
                  </tr>
                  <tr>
                    <td><input class="uk-checkbox" type="checkbox" aria-label="Checkbox"></td>
                    <td>
                      <img class="uk-preserve-width uk-border-circle" src="../asserts/dark_field_cali.png" width="40" height="40" alt="">
                    </td>
                    <td class="uk-table-link">
                      <a class="uk-link-reset" href="#" @click="clickMe">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.</a>
                    </td>
                    <td class="uk-text-truncate">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.</td>
                    <td class="uk-text-nowrap">Lorem ipsum dolor</td>
                  </tr>
                  <tr>
                    <td><input class="uk-checkbox" type="checkbox" aria-label="Checkbox"></td>
                    <td>
                      <img class="uk-preserve-width uk-border-circle" src="../asserts/dark_field_cali.png" width="40" height="40" alt="">
                    </td>
                    <td class="uk-table-link">
                      <a class="uk-link-reset" href="#" @click="clickMe">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.</a>
                    </td>
                    <td class="uk-text-truncate">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.</td>
                    <td class="uk-text-nowrap">Lorem ipsum dolor</td>
                  </tr>
                  <tr>
                    <td><input class="uk-checkbox" type="checkbox" aria-label="Checkbox"></td>
                    <td>
                      <img class="uk-preserve-width uk-border-circle" src="../asserts/dark_field_cali.png" width="40" height="40" alt="">
                    </td>
                    <td class="uk-table-link">
                      <a class="uk-link-reset" href="#" @click="clickMe">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.</a>
                    </td>
                    <td class="uk-text-truncate">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.</td>
                    <td class="uk-text-nowrap">Lorem ipsum dolor</td>
                  </tr>

                  <tr>
                    <td><input class="uk-checkbox" type="checkbox" aria-label="Checkbox"></td>
                    <td>
                      <img class="uk-preserve-width uk-border-circle" src="../asserts/dark_field_cali.png" width="40" height="40" alt="">
                    </td>
                    <td class="uk-table-link">
                      <a class="uk-link-reset" href="#" @click="clickMe">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.</a>
                    </td>
                    <td class="uk-text-truncate">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.</td>
                    <td class="uk-text-nowrap">Lorem ipsum dolor</td>
                  </tr>
                  <tr>
                    <td><input class="uk-checkbox" type="checkbox" aria-label="Checkbox"></td>
                    <td>
                      <img class="uk-preserve-width uk-border-circle" src="../asserts/dark_field_cali.png" width="40" height="40" alt="">
                    </td>
                    <td class="uk-table-link">
                      <a class="uk-link-reset" href="#" @click="clickMe">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.</a>
                    </td>
                    <td class="uk-text-truncate">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.</td>
                    <td class="uk-text-nowrap">Lorem ipsum dolor</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "DarkFieldCali",

  methods: {
    clickMe(event) {
      console.log("clicked a dark field calibration item.")
    }
  }
}
</script>