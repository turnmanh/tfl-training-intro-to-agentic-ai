<template>
    <div :class="gridClasses">
        <slot />
    </div>
</template>

<script setup>
import { tv } from "tailwind-variants";
import { computed } from "vue";

const props = defineProps({
    columns: { default: 1 },
    gap: { default: "md" },
    width: { default: "full" },
});

const grid = tv({
    base: "grid mx-auto",
    variants: {
        columns: {
            1: "grid-cols-1",
            2: "grid-cols-2",
            3: "grid-cols-3",
            4: "grid-cols-4",
            5: "grid-cols-5",
            6: "grid-cols-6",
            7: "grid-cols-7",
            8: "grid-cols-8",
            9: "grid-cols-9",
            10: "grid-cols-10",
            11: "grid-cols-11",
            12: "grid-cols-12",
        },
        gap: {
            none: "",
            sm: "grid-gap-3",
            md: "grid-gap-5",
            lg: "grid-gap-8",
        },
        width: {
            full: "w-full",
            100: "w-full",
            90: "w-9/10",
            80: "w-8/10",
            70: "w-7/10",
            60: "w-6/10",
            50: "w-5/10",
        },
    },
});

const gridClasses = computed(() => grid(props));
</script>
