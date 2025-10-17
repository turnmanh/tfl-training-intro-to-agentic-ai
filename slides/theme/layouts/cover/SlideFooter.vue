<template>
    <div class="h-22 flex flex-row justify-end">
        <div class="flex flex-col justify-center">
            <img class="w-60 mr-5" :src="endorsementLogoUrl" alt="" />
        </div>
    </div>
</template>

<script setup>
const endorsementLogoUrl = new URL(
    "../../assets/endorsement_logo_white.png",
    import.meta.url,
).href;
</script>
