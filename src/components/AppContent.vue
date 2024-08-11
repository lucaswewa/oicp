<template>
  <div
    id="app-content"
    class="uk-margin-remove uk-padding-remove uk-height-1-1"
    uk-grid
  >
    <div id="navigator-container">
      <div 
        id="navigator"
        class="uk-flex uk-flex-column uk-padding-remove uk-width-auto uk-height-1-1 uk-text-center"
      >
        <template v-for="(item, index) in navigatorTabs">
          <TabIcon 
            :id="item.id" 
            :tabID="item.id" 
            :title="item.title" 
            :currentTab="currentTab"
            @setTab="setTab"
          >
            <i class="material-icons">{{ item.icon }}</i>
          </TabIcon>
        </template>
      </div>
    </div>

    <div
      id="content-container"
      class="uk-padding-remove uk-height-1-1 uk-width-expand"
    >
      <TabContent
        v-for="item in navigatorTabs"
        :id="item.id + 'tab-content'"
        :tabID="item.id"
        :currentTab="currentTab"
      >
        <component :is="item.component"></component>
      </TabContent>
    </div>
  </div>

</template>

<script>
import TabIcon from './tabControl/TabIcon.vue';
import TabContent from './tabControl/TabContent.vue';

import HomeContent from './HomeContent.vue'
import MeasurementControl from './measurementControl/measurementControl.vue';
import CaptureContent from './instrumentControl/instrumentControl.vue';
import CalibrationControl from './calibrationControl/calibrationControl.vue';
import StageContent from './StageContent.vue';
import GalleryContent from './GalleryContent.vue';
import SettingsContent from './settingsControl/SettingsContent.vue';
import ViewControl from './streamControl/viewControl.vue';

export default {
  name: "AppContent",

  components: {
    TabIcon,
    TabContent,
    HomeContent,
    MeasurementControl,
    CaptureContent,
    StageContent,
    GalleryContent,
    SettingsContent,
    ViewControl
  },

  data: function() {
    return {
      currentTab: "home"
    }
  },

  computed: {
    navigatorTabs: function() {
      return [
      {
          id: "home",
          icon: "home",
          title: "Home",
          component: HomeContent
        },
        {
          id: "view",
          icon: "visibility",
          title: "View",
          component: ViewControl
        },
        {
          id: "measurement",
          icon: "monochrome_photos",
          title: "Measure",
          component: MeasurementControl
        },
        {
          id: "capture",
          icon: "camera",
          title: "Instrument",
          component: CaptureContent
        },
        {
          id: "calibration",
          icon: "star",
          title: "Calibration",
          component: CalibrationControl
        },
        {
          id: "gallery",
          icon: "photo_library",
          title: "Results",
          component: GalleryContent
        },
        {
          id: "settings",
          icon: "settings",
          title: "Settings",
          component: SettingsContent
        },
        {
          id: "stage",
          icon: "gamepad",
          title: "Stage",
          component: StageContent
        }
      ]
    }
  },

  methods: {
    setTab: function(event, tab) {
      this.currentTab = tab
      console.log("From AppContent" + this.currentTab)
    }
  }
};
</script>