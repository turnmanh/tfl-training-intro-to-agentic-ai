<template>
    <BaseSlide
        :title="$frontmatter.title"
        :subtitle="$frontmatter.subtitle"
        :lines="$frontmatter.lines"
    >
        <TwoColumns
            :span="$frontmatter.span"
            :left-align="leftAlign"
            :right-align="rightAlign"
            :left-justify="leftJustify"
            :right-justify="rightJustify"
        >
            <template #left>
                <slot name="left" />
            </template>
            <template #right>
                <slot name="right" />
            </template>
        </TwoColumns>
    </BaseSlide>
</template>

<script setup>
import BaseSlide from "./base/BaseSlide.vue";
import TwoColumns from "./columns/TwoColumns.vue";

import { useSlideContext } from "@slidev/client";

const { $frontmatter } = useSlideContext();

function getColumnProperties(p) {
    if (typeof p === "string") {
        // single value for both columns
        return {
            left: p,
            right: p,
        };
    } else if (Array.isArray(p) && p.length === 2) {
        // different values for the columns
        return {
            left: p[0],
            right: p[1],
        };
    } else {
        // defaults, or on error
        return {
            left: "",
            right: "",
        };
    }
}

const { left: leftAlign, right: rightAlign } = getColumnProperties(
    $frontmatter.align,
);

const { left: leftJustify, right: rightJustify } = getColumnProperties(
    $frontmatter.justify,
);
</script>
