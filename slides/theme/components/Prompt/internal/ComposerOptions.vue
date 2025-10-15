<template>
    <div class="h-7 flex flex-row gap-1 px-2 mb-2">
        <ToolSelector :tool="props.tool" />

        <div class="flex-1"></div>

        <DictateButton />
        <SubmitButton @submit="$emit('submit')" />
    </div>
</template>

<script setup>
import ToolSelector from "./ToolSelector.vue";
import DictateButton from "./buttons/DictateButton.vue";
import SubmitButton from "./buttons/SubmitButton.vue";

const props = defineProps({
    tool: { default: "" },
});

defineEmits(["submit"]);
</script>
