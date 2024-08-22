<template>
  <div uk-grid class="uk-height-1-1 uk-margin-remove uk-padding-remove">
		<div class="settings-nav">
      <ul class="uk-nav uk-nav-default">
        <li class="uk-nav-header">Calibration Cat1</li>
        <li>
          <TabIcon
            id="settings-display-icon"
            tabID="Dark Field Calibration"
            :currentTab="currentTab"
            @setTab="setTab"
          >
            <i class="material-icons">photo_camera</i>
          </TabIcon>
        </li>
        <li>
          <TabIcon
            id="settings-general-icon"
            tabID="Distortion Calibration"
            :currentTab="currentTab"
            @setTab="setTab"
          >
            <i class="material-icons">photo_camera</i>
          </TabIcon>
        </li>

        <li>
          <TabIcon
            id="settings-features-icon"
            tabID="Flat Field Calibration"
            :currentTab="currentTab"
            @setTab="setTab">
            <i class="material-icons">photo_camera</i>
          </TabIcon>
        </li>
        <li>
          <TabIcon
            id="settings-camera-icon"
            tabID="Color Shift Calibration"
            :currentTab="currentTab"
            @setTab="setTab"
          >
            <i class="material-icons">photo_camera</i>
          </TabIcon>
        </li>
        <li class="uk-nav-header">Calibration Cat2</li>
        <li>
          <TabIcon
            id="settings-stage-icon"
            tabID="Multi-Point Calibration"
            :currentTab="currentTab"
            @setTab="setTab"
          >
            <i class="material-icons">photo_camera</i>
          </TabIcon>
        </li>
        <li>
          <TabIcon
            id="settings-general-icon"
            tabID="Stray-Light Calibration"
            :currentTab="currentTab"
            @setTab="setTab"
          >
            <i class="material-icons">photo_camera</i>
          </TabIcon>
        </li>
        <li>
          <TabIcon
            id="settings-general-icon"
            tabID="Image Scaling Calibration"
            :currentTab="currentTab"
            @setTab="setTab"
          >
            <i class="material-icons">photo_camera</i>
          </TabIcon>
        </li>
        <li>
          <TabIcon
            id="settings-general-icon"
            tabID="Single Filter Calibration"
            :currentTab="currentTab"
            @setTab="setTab"
          >
            <i class="material-icons">photo_camera</i>
          </TabIcon>
        </li>
        <li>
          <TabIcon
            id="settings-general-icon"
            tabID="One Color Calibration"
            :currentTab="currentTab"
            @setTab="setTab"
          >
            <i class="material-icons">photo_camera</i>
          </TabIcon>
        </li>
        <li>
          <TabIcon
            id="settings-general-icon"
            tabID="Four Color Calibration"
            :currentTab="currentTab"
            @setTab="setTab"
          >
            <i class="material-icons">photo_camera</i>
          </TabIcon>
        </li>
        <li>
          <TabIcon
            id="settings-general-icon"
            tabID="Brightness Rescaling Calibration"
            :currentTab="currentTab"
            @setTab="setTab"
          >
            <i class="material-icons">photo_camera</i>
          </TabIcon>
        </li>

      </ul>
    </div>

    <div class="view-component uk-width-expand uk-padding-small">
      <TabContent
        tabID="Dark Field Calibration"
        :currentTab="currentTab"
      >
        <div class="settings-pane uk-padding-small">
          <DarkFieldCalibrationControl/>
        </div>
      </TabContent>
    </div>
	</div>
</template>

<script>
import CalibrationControlPanel from './calibrationControlPanel.vue';
import TabContent from '../tabControl/TabContent.vue';
import TabIcon from '../tabControl/TabIcon.vue';

import DarkFieldCalibrationControl from './darkFieldCalibrationControl.vue';

export default {
  name: "Calibration Content",

  components: {
    TabIcon,
    TabContent,
    CalibrationControlPanel,
    DarkFieldCalibrationControl
  },

  data: function() {
    return {
      selected: "display",
      currentTab: "display"
    }
  },

  methods: {
    setTab: function(event, tab) {
      if (!(this.currentTab == tab)) {
        this.currentTab = tab
      }
    }
  }
}
</script>

<style lang="less" scoped>
// Custom UIkit CSS modifications
@import "../../assets/less/theme.less";

.settings-nav {
  overflow-y: auto;
  overflow-x: hidden;
  width: 250px;
  padding: 10px;
  background-color: rgba(180, 180, 180, 0.03);
  border-width: 0 1px 0 0;
  border-style: solid;
  border-color: rgba(180, 180, 180, 0.25);
}

.settings-nav li > a {
  padding-left: 6px !important;
  border-radius: @button-border-radius;
}
</style>