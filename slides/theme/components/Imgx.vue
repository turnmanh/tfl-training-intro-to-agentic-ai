<template>
    <img :class="imgClasses" :src="props.src" alt="" />
    <p :class="captionClasses">
        <slot />
    </p>
</template>

<script setup>
import { computed } from "vue";
import { tv } from "tailwind-variants";

const imgx = tv({
    base: "",
    variants: {
        width: {
            full: "w-full",
            100: "w-full",
            95: "w-95/100",
            90: "w-90/100",
            85: "w-85/100",
            80: "w-80/100",
            75: "w-75/100",
            70: "w-70/100",
            65: "w-65/100",
            60: "w-60/100",
            55: "w-55/100",
            50: "w-50/100",
            45: "w-45/100",
            40: "w-40/100",
            35: "w-35/100",
            30: "w-30/100",
            25: "w-25/100",
            20: "w-20/100",
            15: "w-15/100",
        },
        align: {
            left: "mr-auto",
            center: "mx-auto",
            right: "ml-auto",
        },
    },
});

const caption = tv({
    base: "text-xs mt-3",
    variants: {
        align: {
            left: "text-left",
            center: "text-center",
            right: "text-right",
        },
    },
});

const props = defineProps({
    src: {},
    width: { default: 100 },
    align: { default: "center" },
});

const imgClasses = computed(() => imgx(props));

const captionClasses = computed(() => caption(props));
</script>
