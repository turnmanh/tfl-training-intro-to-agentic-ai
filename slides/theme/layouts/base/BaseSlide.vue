<template>
    <div class="flex flex-col h-full bg-aai-slide">
        <!-- header -->
        <SlideHeader :title="props.title" :subtitle="props.subtitle" />

        <!-- content -->
        <div class="bg-aai-slide text-aai-blue flex-1 p-15 pb-7">
            <div class="content h-full">
                <Field
                    height="full"
                    :text="props.text"
                    :justify="props.justify"
                    :align="align"
                >
                    <slot />
                </Field>
            </div>
        </div>

        <!-- footer -->
        <SlideFooter />
    </div>

    <!-- optional: lines overlay -->
    <img
        class="w-40 absolute top-90 -left-1"
        v-if="$frontmatter.lines"
        src="../../assets/lines_blue.png"
        alt=""
    />
</template>

<script setup>
import SlideHeader from "./SlideHeader.vue";
import SlideFooter from "./SlideFooter.vue";

const props = defineProps({
    title: {},
    subtitle: { default: "" },
    lines: { default: false },
    text: {},
    justify: {},
    align: {},
});

const align = props.align === "center" ? "offcenter" : props.align;
</script>
