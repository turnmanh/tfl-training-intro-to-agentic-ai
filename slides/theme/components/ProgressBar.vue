<template>
  <div class="w-3/4 my-10 mx-auto bg-white border-3 border-[#084059] rounded-full h-10 flex items-center p-1">
    <div
      class="h-full bg-[#3FC1C9] rounded-full transition-all duration-300"
      :style="{ width: percent + '%' }"
    ></div>
  </div>
</template>

<script setup>
const props = defineProps({
  percent: {
    type: Number,
    default: 0,
  },
});
</script>
