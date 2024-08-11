<template>
  <div uk-grid class="uk-height-1-1 uk-margin-remove uk-padding-remove">
    <div class="settings-nav">
      <ul class="uk-nav uk-nav-default">
        <li class="uk-nav-header">Application Settings</li>
        <li>
          <TabIcon
            id="settings-display-icon"
            tabID="display"
            :currentTab="currentTab"
            @setTab="setTab"
          >
            <i class="material-icons">desktop_windows</i>
          </TabIcon>
        </li>
        <li>
          <TabIcon
            id="settings-features-icon"
            tabID="features"
            :currentTab="currentTab"
            @setTab="setTab"
          >
            <i class="material-icons">settings_input_component</i>
          </TabIcon>
        </li>
        <li class="uk-nav-header">MS Settings</li>
        <li>
          <TabIcon
            id="settings-camera-icon"
            tabID="camera"
            :currentTab="currentTab"
            @setTab="setTab"
          >
            <i class="material-icons">photo_camera</i>
          </TabIcon>
        </li>
        <li>
          <TabIcon
            id="settings-stage-icon"
            tabID="stage"
            :currentTab="currentTab"
            @setTab="setTab"
          >
            <i class="material-icons">home</i>
          </TabIcon>
        </li>
        <li>
          <TabIcon
            id="settings-general-icon"
            tabID="general"
            :currentTab="currentTab"
            @setTab="setTab"
          >
            <i class="material-icons">exit_to_app</i>
          </TabIcon>
        </li>
      </ul>
    </div>
    <div class="view-component uk-width-expand uk-padding-small">
      <TabContent
        tabID="display"
        :currentTab="currentTab"
      >
        <div class="settings-pane uk-padding-small">
          <AppSettingsContent/>
          <StreamSettingsContent/>
        </div>
      </TabContent>

      <TabContent
        tabID="features"
        :currentTab="currentTab"
      >
        <div class="settings-pane uk-padding-small">
          <FeaturesSettingsContent/>
        </div>
      </TabContent>

      <TabContent
        tabID="camera"
        :currentTab="currentTab"
      >
        <div class="settings-pane uk-padding-small">
          <CameraSettingsContent/>
        </div>
      </TabContent>

      <TabContent
        tabID="stage"
        :currentTab="currentTab"
      >
        <div class="settings-pane uk-padding-small">
          <StageSettingsContent/>
        </div>
      </TabContent>

      <TabContent
        tabID="general"
        :currentTab="currentTab"
      >
        <div class="settings-pane uk-padding-small">
          <OicpSettingsContent/>
        </div>
      </TabContent>
    </div>
  </div>
</template>

<script>
import AppSettingsContent from './AppSettingsContent.vue';
import CalibrationSettingsContent from './CalibrationSettingsContent.vue';
import CameraSettingsContent from './CameraSettingsContent.vue';
import FeaturesSettingsContent from './FeaturesSettingsContent.vue';
import OicpSettingsContent from './OicpSettingsContent.vue';
import StageSettingsContent from './StageSettingsContent.vue';
import StreamSettingsContent from './StreamSettingsContent.vue';
import TabContent from './TabContent.vue';
import TabIcon from './TabIcon.vue';

export default {
  name: "Settings Content",

  components: {
      TabIcon,
      TabContent,
      CameraSettingsContent,
      StreamSettingsContent,
      CameraSettingsContent,
      AppSettingsContent,
      FeaturesSettingsContent,
      CalibrationSettingsContent,
      StageSettingsContent,
      OicpSettingsContent
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
@import "../assets/less/theme.less";

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