<template>
    <div :class="promptEditorClasses" ref="promptContainer">
        <slot />
    </div>
</template>

<style>
.prompt {
    pre {
        @apply m-0 whitespace-pre-wrap break-words;

        code {
            @apply font-[Arial] text-black text-xs leading-none;
        }
    }
}
</style>

<script setup>
import { ref, computed } from "vue";
import { tv } from "tailwind-variants";

const promptEditor = tv({
    base: "prompt overflow-auto pb-1 mt-3 mb-2 mx-4 [line-height:1] [scrollbar-width:none] [&::-webkit-scrollbar]:hidden",
    variants: {
        size: {
            auto: "max-h-60",
            xs: "h-10",
            sm: "h-20",
            md: "h-30",
            lg: "h-40",
            xl: "h-50",
        },
    },
});

const props = defineProps({
    size: { default: "auto" },
});

const promptEditorClasses = computed(() => promptEditor(props));

const promptContainer = ref(null);

function getPrompt() {
    const element = promptContainer.value?.querySelector("pre code");
    return element?.textContent || "";
}

defineExpose({ getPrompt });
</script>
