<template>
    <p>Stage Settings Content</p>
    <p>Client Side Route</p>
    <a href="#/route1">R1</a> |
    <a href="#/route2">R2</a> |
    <a href="#/route3">R3</a>
    <component :is="currentView" />

    <hr />

    <button id="show-modal" @click="showModal = true">Show Modal</button>

    <Teleport to="body">
        <!-- use the modal component, pass in the prop -->
        <modal :show="showModal" @close="showModal = false">
            <template #header>
            <h3>Custom Header</h3>
            </template>
        </modal>
    </Teleport>

    <p>Has published books:</p>
    <span>{{ publishedBooksMessage }}</span>
    <div :class="{ active: isActive }">
        <p>active?</p>
    </div>
    <button @click="increment" class="uk-button uk-button-primary uk-margin uk-margin-remove-top uk-width-1-1">
        {{  count }}
    </button>
    <button @click="increment2" class="uk-button uk-button-primary uk-margin uk-margin-remove-top uk-width-1-1">
        {{  state.count }}
    </button>

    <hr/>

    <p>Message is: {{  message }}</p>
    <input v-model="message" placeholder="edit me" class="uk-input uk-form-small" />
    <textarea v-model="message" placeholder="add multiple lines" class="uk-input uk-form-small"></textarea>

    <hr />
    <input type="checkbox" id="checkbox" class="uk-checkbox" v-model="checked" />
    <label for="checkbox">{{ checked ? "checked" : "unchecked" }}</label>

    <hr />
    <div>Checked names: {{ checkedNames }}</div>
    <div class="uk-grid-small uk-child-width-1-3" uk-grid>
        <div>
            <input type="checkbox" id="jack" value="Jack" v-model="checkedNames" class="uk-checkbox" />
            <label for="jack">Jack</label>
        </div>
        <div>
            <input type="checkbox" id="john" value="John" v-model="checkedNames" class="uk-checkbox" />
            <label for="john">John</label>
        </div>
        <div>
            <input type="checkbox" id="mike" value="Mike" v-model="checkedNames" class="uk-checkbox" />
            <label for="mike">Mike</label>
        </div>
    </div>

    <hr />
    <div>Picked: {{ picked }}</div>
    <div class="uk-grid-small uk-child-width-1-3" uk-grid>
        <div>
            <input type="radio" id="color-x" value="X" v-model="picked" class="uk-radio" />
            <label for="color-x">X</label>
        </div>
        <div>
            <input type="radio" id="color-y" value="Y" v-model="picked" class="uk-radio" />
            <label for="color-y">Y</label>
        </div>
        <div>
            <input type="radio" id="color-z" value="Z" v-model="picked" class="uk-radio" />
            <label for="color-z">Z</label>
        </div>
    </div>

    <hr />
    <div>Selected: {{ selected }}</div>
    <select v-model="selected" class="uk-select" @change="console.log('ccc')">
        <option>Clear</option>
        <option>ND1</option>
        <option>ND2</option>
        <option>ND3</option>
    </select>

    <hr />
    <div>Multi Select: {{ multiselected }}</div>
    <select v-model="multiselected" multiple class="uk-select">
        <option>A</option>
        <option>B</option>
        <option>C</option>
    </select>
</template>

<script setup>
import { ref, reactive, computed, nextTick, onMounted } from 'vue';
import Modal from './Modal.vue'
import R1 from './route1.vue'
import R2 from './route2.vue'
import R3 from './route3.vue'

const routes = {
    "/route1": R1,
    "/route2": R2,
    "/route3": R3
}

const currentPath = ref(window.location.hash)

window.addEventListener('hashchange', () => {
    currentPath.value = window.location.hash
})

const currentView = computed(() => {
    return routes[currentPath.value.slice(1) || "/"]
})
const showModal = ref(false)

const props = defineProps({
    foo: { type: String, required: true },
    bar: Number
})

props.foo
props.bar

const selected = ref("Clear")

const picked = ref("One")

const checked = ref(true)

const checkedNames = ref([])

const multiselected = ref([])

const isActive = ref(true)
const count = ref(0)
const state = reactive({ count: 0})
const author = reactive({
    name: "John Doe",
    books: [
        "Vue 2 - Advanced Guide",
        "Vue 3 - Basic Guide",
        "Vue 4 - The Mystery"
    ]
})

const publishedBooksMessage = computed(() => {
    return author.books.length > 0 ? "Yes" : "No"
})

const message = ref("Hello world")
async function increment(event) {
    count.value++
    await nextTick()
}

async function increment2() {
    state.count++
}

onMounted(() => {
    console.log("Mounted.")
})
</script>