<template>
    <div class="h-22 bg-white flex flex-row flex-none">
        <!-- title -->
        <div class="flex flex-col justify-center flex-1 px-7">
            <h1
                class="text-aai-blue text-xl font-semibold"
                v-html="props.title"
            ></h1>
            <p v-if="props.subtitle" class="text-aai-blue text-lg -mt-1">
                {{ props.subtitle }}
            </p>
        </div>
        <!-- logo -->
        <div class="flex flex-col justify-center">
            <img class="w-40" :src="logoUrl" alt="" />
        </div>
    </div>
</template>

<script setup>
const props = defineProps({
    title: {},
    subtitle: { default: "" },
});

const logoUrl = new URL("../../assets/aai_logo_color.png", import.meta.url)
    .href;
</script>
