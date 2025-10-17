<template>
    <button :class="buttonClasses" @click="onClick">
        <slot />
    </button>
</template>

<script setup>
import { computed } from "vue";
import { tv } from "tailwind-variants";

const button = tv({
    base: "w-7 h-7 rounded-full flex flex-row justify-center items-center leading-none",
    variants: {
        color: {
            white: "bg-white hover:bg-gray-100 text-black",
            black: "bg-black text-white",
        },
    },
});

const props = defineProps({
    color: { default: "white" },
});

const buttonClasses = computed(() => button(props));

const emit = defineEmits(["click"]);

function onClick() {
    emit("click");
}
</script>
