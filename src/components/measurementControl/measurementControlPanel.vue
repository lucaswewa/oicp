<template>
  <div>
    <ul>
      <li>measurement setup
        <ul>
          <li>camera settings: binning, subframe region in pixels</li>
          <li>Capture settings
            <ul>
              <li>Focus mode</li>
              <li>adjust exposure</li>
              <li>exposure time with XYZ and ND filters (FE)</li>
            </ul>
          </li>
          <li>Calibration settings
            <ul>
              <li>brightness scalling / Color Calibration</li>
              <li>Image Scaling Calibration</li>
              <li>Flat Field Calibration</li>
            </ul>
          </li>
          <li>measurement settings
            <ul>
              <li>distance unit: m/cm/mm/um/ft/in</li>
              <li>photometric unit: cd/m2, fL, knit, Mnit, mcd/cm2 mNit, nit</li>
            </ul>
          </li>
          <li>Post-measurement operations
            <ul>
              <li>register active display area</li>
              <li>remove moire</li>
              <li>show histogram, 2D Iso Plot, CIE Color Chart, Analysis Form</li>
            </ul>
          </li>
          <li>Measurement Information
            <ul>
              <li>notes</li>
              <li>timestamp</li>
            </ul>
          </li>
        </ul>
      </li>


      <li>Select HW Settings: AE/FE, ND, RX, Focusing, etc</li>
      <li>Select Calibratioin Profiles</li>
      <li>Select Measurement Type: Four-color, One-color</li>
      <li>Optional: Select Light Source</li>
      <li>Define point of interest</li>
      <li>Make Measurement</li>
      <li>Measurement operation
        <ul>
          <li>add</li>
          <li>subtract</li>
          <li>multiplication</li>
        </ul>
      </li>
      <li>Export data</li>
    </ul>
  </div>
</template>