<template>
    <div class="h-22 flex flew-row justify-end">
        <div class="flex flex-col justify-center">
            <img class="w-40" :src="logoUrl" alt="" />
        </div>
    </div>
</template>

<script setup>
const logoUrl = new URL("../../assets/aai_logo_white.png", import.meta.url)
    .href;
</script>
