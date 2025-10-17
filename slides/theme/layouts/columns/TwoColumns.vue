<template>
    <Grid columns="12">
        <Field
            height="80"
            :span="props.span"
            :align="props.leftAlign"
            :justify="props.leftJustify"
        >
            <slot name="left" />
        </Field>
        <Field
            height="80"
            :span="12 - props.span"
            :align="props.rightAlign"
            :justify="props.rightJustify"
        >
            <slot name="right" />
        </Field>
    </Grid>
</template>

<script setup>
import { computed } from "vue";

const props = defineProps({
    span: { default: 6 },
    leftAlign: { default: "top" },
    rightAlign: { default: "top" },
    leftJustify: { default: "left" },
    rightJustify: { default: "left" },
});
</script>
