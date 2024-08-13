<template>
  <div>
    <ul>
      <li>Calibratioin Profile List
        <ul>
          <li>Image Scaling Calibration: pixel to object_size_in_meters, this is related to lens EFL and distortion correction</li>
          <li>Lens Distortion Calibration</li>
          <li>Flat Field Calibration</li>
          <li>Color shift correction</li>
          <li>Stray-Light Calibration</li>
        </ul>
      </li>
      <hr />
      <li>Dark Field Calibration</li>
      <li>Flat Field Calibration
        <ul>
          <li>Spectra range: Photometric or Radiometric</li>
          <li>Type: Luminance and Illuminance</li>
          <li>Binning for hori/vert</li>
          <li>Uniform Luminance Source (ULS): IS for luminance FFC</li>
          <li>A separate calibraiton record is registered for each F-stop of each lens</li>
          <li>Calibration lamp to create a cosine pattern on a Lambertian screen: for illuminance FFC</li>
        </ul>
      </li>
      <li>Color Shift Calibration
        <ul>
          <li>Color Filters: X/Y/Z/?</li>
          <li>ND Filters: Clear/ND1/ND2/...</li>
          <li>ShiftX</li>
          <li>ShiftY</li>
        </ul>
      </li>
      <li>Multi-point Calibration
        <ul>
          <li>To meet the industry standards for measurement of flat panels</li>
          <li>Interpolation method: Cubic Spline, Nearest Neighbor</li>
          <li>number filters: one filter: photopic; three filters: brightness and chromaticity</li>
        </ul>
      </li>
      <li>Stray-Light Calibration
        <ul>
          <li>interpolation method</li>
          <li>number filters</li>
        </ul>
      </li>
      <li>Image Scaling Calibration
        <ul>
          <li>pixel to object size in meters, related to EFL and distortion correction</li>
        </ul>
      </li>
      <li>Single Filter Brightness Scaling Calibration
        <ul>
          <li>Color Filters: X/Y/Z</li>
          <li>ND filters: Clear/ND1/ND2/../ND5</li>
        </ul>
      </li>
      <li>Distortion Calibratioin
        <ul>
          <li>NumberX</li>
          <li>NumberY</li>
          <li>Xmin</li>
          <li>Ymin</li>
          <li>Xmax</li>
          <li>Ymax</li>
          <li>CameraOrientation</li>
          <li>CameraMirror</li>
        </ul>
      </li>
      <li>One-color Calibration
        <ul>
          <li>...</li>
        </ul>
      </li>
      <li>Four-color Calibration
        <ul>
          <li>ND</li>
          <li>Exposure</li>
          <li>Measurement points: location, size, circle/rectangle</li>
          <li>Color Space: CxCy(CIE1931), u'v'(CIE1976)</li>
          <li>Measure Color Points</li>
        </ul>
      </li>
      <li>Brightness Rescaling
        <ul>
          <li>Color Filters: X/Y/Z</li>
          <li>ND Filters: Clear/ND1/ND2/../ND5</li>
        </ul>
      </li>
      <li>Adaptive Select Color Calibration
        <ul>
          <li>...</li>
        </ul>
      </li>
    </ul>
  </div>
</template>