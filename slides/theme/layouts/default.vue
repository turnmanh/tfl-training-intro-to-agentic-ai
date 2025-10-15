<template>
    <BaseSlide
        :title="$frontmatter.title"
        :subtitle="$frontmatter.subtitle"
        :lines="$frontmatter.lines"
        :text="$frontmatter.text"
        :justify="$frontmatter.justify"
        :align="$frontmatter.align"
    >
        <slot />
    </BaseSlide>
</template>

<script setup>
import { useSlideContext } from "@slidev/client";

import BaseSlide from "./base/BaseSlide.vue";

const { $frontmatter } = useSlideContext();
</script>
