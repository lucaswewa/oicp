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
        <p>{{ item.id }}</p>
      </TabContent>
    </div>
  </div>

</template>

<script>
import TabIcon from './TabIcon.vue';
import TabContent from './TabContent.vue'

export default {
  name: "AppContent",

  components: {
    TabIcon,
    TabContent
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