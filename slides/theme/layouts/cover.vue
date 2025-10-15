<template>
    <CoverSlide
        :title="$frontmatter.title"
        :subtitle="$frontmatter.subtitle"
        :tag="$frontmatter.tag"
    >
        <slot />
    </CoverSlide>
</template>

<script setup>
import { useSlideContext } from "@slidev/client";

import CoverSlide from "./cover/CoverSlide.vue";

const { $frontmatter } = useSlideContext();
</script>
