<template>
    <div
        class="h-7 px-2 rounded-full flex flex-row gap-1 items-center font-[Arial] text-[0.7rem] text-[#0285ff] hover:bg-[#f5faff]"
    >
        <Icon />
        <span>{{ toolName }}</span>
        <CloseIcon />
    </div>
</template>

<style>
:host {
    --tool-blue: #0285ff;
}
</style>

<script setup>
import { computed } from "vue";

import AgentIcon from "./AgentIcon.vue";
import CanvasIcon from "./CanvasIcon.vue";
import ImageIcon from "./ImageIcon.vue";
import ResearchIcon from "./ResearchIcon.vue";
import SearchIcon from "./SearchIcon.vue";
import StudyIcon from "./StudyIcon.vue";
import CloseIcon from "./CloseIcon.vue";

const icons = {
    agent: AgentIcon,
    canvas: CanvasIcon,
    image: ImageIcon,
    research: ResearchIcon,
    search: SearchIcon,
    study: StudyIcon,
};

const props = defineProps({
    tool: { default: "" },
});

const Icon = AgentIcon;

const toolName = computed(() => "Agent");
</script>
