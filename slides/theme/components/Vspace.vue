<template>
    <div :class="vspaceClasses"></div>
</template>

<script setup>
import { computed } from "vue";

import { tv } from "tailwind-variants";

const vspace = tv({
    base: "",
    variants: {
        size: {
            xs: "h-1",
            sm: "h-3",
            md: "h-5",
            lg: "h-7",
            xl: "h-9",
            "2xl": "h-11",
            "3xl": "h-13",
            "3xl": "h-15",
            "4xl": "h-17",
        },
    },
});

const props = defineProps({
    size: { default: "md" },
});

const vspaceClasses = computed(() => vspace(props));
</script>
