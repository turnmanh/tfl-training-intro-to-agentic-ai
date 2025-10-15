<template>
    <div :class="boxClasses">
        <div class="whitespace-normal min-w-0">
            <slot />           
        </div>
    </div>
</template>

<script setup>
import { computed } from "vue";

import { tv } from "tailwind-variants";

const box = tv({
    base: "rounded-lg p-3 flex flex-col",
    variants: {
        span: {
            1: "col-span-1",
            2: "col-span-2",
            3: "col-span-3",
            4: "col-span-4",
            5: "col-span-5",
            6: "col-span-6",
            7: "col-span-7",
            8: "col-span-8",
            9: "col-span-9",
            10: "col-span-10",
            11: "col-span-11",
            12: "col-span-12",
        },
        start: {
            auto: "",
            1: "col-start-1",
            2: "col-start-2",
            3: "col-start-3",
            4: "col-start-4",
            5: "col-start-5",
            6: "col-start-6",
            7: "col-start-7",
            8: "col-start-8",
            9: "col-start-9",
            10: "col-start-10",
            11: "col-start-11",
            12: "col-start-12",
        },
        height: {
            auto: "",
            20: "h-20",
            25: "h-25",
            30: "h-30",
            35: "h-35",
            40: "h-40",
            45: "h-45",
            50: "h-50",
            55: "h-55",
            60: "h-60",
            65: "h-65",
            70: "h-70",
            75: "h-75",
            80: "h-80",
            85: "h-85",
        },
        color: {
            white: "bg-white text-aai-blue",
            grey: "bg-aai-box-grey text-aai-blue",
            blue: "bg-aai-box-blue text-aai-blue",
            "dark-blue": "bg-aai-blue text-white",
            "light-gray": "bg-gray-100 text-aai-blue",
        },
        text: {
            sm: "text-xs",
            md: "text-sm",
            lg: "text-md",
        },
        justify: {
            left: "text-left",
            center: "text-center",
            justify: "text-justify",
            right: "text-right",
        },
        align: {
            start: "justify-start",
            center: "justify-center",
            end: "justify-end",
        },
    },
});

const props = defineProps({
    span: { default: 1 },
    start: { default: "auto" },
    height: { default: "auto" },
    color: { default: "blue" },
    text: { default: "md" },
    justify: { default: "left" },
    align: { default: "top" },
});

const boxClasses = computed(() => box(props));
</script>
