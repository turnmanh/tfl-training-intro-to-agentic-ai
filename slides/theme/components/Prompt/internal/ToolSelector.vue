<template>
    <div class="flex flex-row items-center gap-1">
        <PlusButton />
        <div v-if="props.tool" class="border-r-1 border-1-gray-300 h-3"></div>
        <Tool v-if="props.tool" :tool="props.tool" />
    </div>
</template>

<script setup>
import PlusButton from "./buttons/PlusButton.vue";
import Tool from "./tools/Tool.vue";

const props = defineProps({
    tool: { default: "" },
});
</script>
