## Declaring Reactive State
Use `ref()` to declare reactive state. `ref()` takes the argument and returns it wrapped within a ref object with a `.value` property.

To access refs in a component's template, declare and return them from a component's `setup()` function.

## Computed Properties
The `computed()` functioin expects to be passed a getter function, and the returned value is a computed ref. Computed properties are cached based on their reactive dependencies.

## Bindings
We can use `v-bind` to bind `class` and `style` attributes.

* `:class` - shortcut for `v-bind:class` to dynamically toggle classes:
```html
<div :class="{ active: isActive }"></div>
```
* `:style`
```html
<div :style="{ color: activeColor, fontSize: fontSize + 'px' }"></div>
```

## Conditioinal Rendering
* `v-if`
* `v-else`
* `v-else-if`
* `v-if` on `<template>` - `v-if` has to be attached to a single element. We can apply it to the `<template>` element as well.
* `v-show`

## List Rending
`v-for` to render a list of items.

```html
<li v-for="item in items">
    {{ item.message }}
</li>
```

## Event Handling
We can use `v-on` (shorten to the `@` symbol) to listen to DOM events. The usage would be `v-on:click="handler"` or `@click="handler"`.

**Event Modifiers**
* `.stop`
* `.prevent`
* `.self`
* `.capture`
* `.once`
* `.passive`

## Form Input Bindings
The `v-model` can be used to bind a model to DOM element.
```html
<input v-model="text">
```

## Lifecycle Hooks

`onMounted`, `onUpdated`, `onUnmounted`

## Listen to Events
`defineEmits` defines emitted events
`defineProps` defines properties

## Content Distributioin with Slots
We can use `<slot>` element to pass content to a component.

## Component Registration
**Global Registration**
```js
app.component(
    'MyComponent',
    {
        /* implementation */
    }
)
```
**Local Registration**
Imported components can be locally used without registration

## State Management
* Simple State Management with Reactivity API - you can use `reactive()` to create a reactive object, and then import it into multiple components.
* Use `Pinia` lib.
