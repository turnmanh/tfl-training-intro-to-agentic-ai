<template>
    <ComposerBox class="mx-auto">
        <!-- user prompt as pre.code -->
        <PromptEditor :size="props.size" ref="promptEditor">
            <slot />
        </PromptEditor>

        <!-- options -->
        <ComposerOptions :tool="props.tool" @submit="copyPrompt" />
    </ComposerBox>
</template>

<script setup>
import { ref } from "vue";

import ComposerBox from "./internal/ComposerBox.vue";
import PromptEditor from "./internal/PromptEditor.vue";
import ComposerOptions from "./internal/ComposerOptions.vue";

const props = defineProps({
    tool: { defaul: "" },
    size: { default: "auto" },
});

const promptEditor = ref(null);

function copyPrompt() {
    const prompt = promptEditor.value?.getPrompt();
    if (prompt) {
        navigator.clipboard.writeText(prompt);
    }
}
</script>
