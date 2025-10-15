<template>
    <div class="bg-aai-blue w-full h-full flex flex-col">
        <SlideHeader />

        <div class="flex flex-row flex-1 items-center">
            <div class="flex-1 -mt-10 ml-20 mr-10">
                <!-- title -->
                <Title v-html="props.title"></Title>

                <!-- subtitle -->
                <Subtitle
                    class="mt-1"
                    v-if="props.subtitle"
                    v-html="props.subtitle"
                ></Subtitle>

                <!-- content -->
                <p class="mt-5 font-light text-white">
                    <slot />
                </p>
            </div>

            <CoverImage />
        </div>

        <Tag class="min-w-60">{{ props.tag }}</Tag>

        <SlideFooter />
    </div>

    <!-- lines overlay -->
    <img
        class="w-40 absolute -top-70 -left-1"
        src="../../assets/lines_white.png"
        alt=""
    />
    <img
        class="w-40 absolute top-90 -left-1"
        src="../../assets/lines_white.png"
        alt=""
    />
</template>

<script setup>
import SlideHeader from "./SlideHeader.vue";

import Title from "./Title.vue";
import Subtitle from "./Subtitle.vue";

import CoverImage from "./CoverImage.vue";
import Tag from "./Tag.vue";

import SlideFooter from "./SlideFooter.vue";

const props = defineProps({
    title: {},
    subtitle: { default: "" },
    tag: { default: "" },
});
</script>
