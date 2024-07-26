<template>
  <div id="app-content">
    <div id="navigator-container">
      <div id="navigator">
        <template v-for="(item, index) in navigatorTabs">
          <TabIcon :id="item.id" :tabID="item.id" :title="item.title" :currentTab="currentTab" @setTab="setTab">
            <i class="material-icons">{{ item.icon }}</i>
          </TabIcon>
        </template>
      </div>
    </div>
  </div>

</template>

<script>
import TabIcon from './TabIcon.vue';

export default {
  name: "AppContent",

  components: {
    TabIcon
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
          component: null
        },
        {
          id: "view",
          icon: "visibility",
          title: "View",
          component: null
        },
        {
          id: "gallery",
          icon: "photo_library",
          title: "Gallery",
          component: null
        },
        {
          id: "move",
          icon: "gamepad",
          title: "Move",
          component: null
        },
        {
          id: "capture",
          icon: "camera",
          title: "Capture",
          component: null
        },
        {
          id: "settings",
          icon: "settings",
          title: "Settings",
          component: null
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
}
</script>