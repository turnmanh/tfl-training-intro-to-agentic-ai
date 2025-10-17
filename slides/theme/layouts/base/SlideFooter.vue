<template>
  <div
    class="absolute bottom-0 right-0 w-full h-8 px-5 text-right text-sm text-aai-blue bg-aai-slide"
  >
    {{ $nav.currentPage }}
  </div>
</template>

<script setup>
import { useSlideContext } from "@slidev/client";
const { $nav } = useSlideContext();
</script>
