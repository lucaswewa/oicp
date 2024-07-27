<template>
	<a
	  href="#"
		class="uk-link"
		:class="classObject"
		@click="clickMe"
	>
	  <slot></slot>
		<div>{{ displayTitle }}</div>
  </a>
</template>

<script>
export default {
	name: "TabIcon",

	props: {
		tabID: {
			type: String,
			required: true
		},
		title: {
			type: String,
			required: false
		},
		currentTab: {
			type: String,
			required: true
		}
	},

	computed: {
		displayTitle: function() {
			if (this.title == undefined) {
				return this.tabID
			} else {
				return this.title
			}
		},
		classObject: function() {
			return {
				"tabicon-active": this.currentTab == this.tabID,
				"uk-disabled": false
			}
		}
	},

	methods: {
		clickMe(event) {
			// emit `setTab` event with this tabID
			this.$emit("setTab", event, this.tabID)
		}
	}
}
</script>

<style lang="less" scoped>
@import "../assets/less/theme.less";

.tabicon-active {
  color: #fff !important;
  background-color: @global-primary-background !important;
}
</style>
