<template>
  <div class="PostDetailCmp">
    <div class="container">
      <div class="heading-wrapper">
        <slot name="title" />
      </div>
      <figure class="post-wrapper">
        <template v-if="slots.image">
          <slot name="image" />
        </template>
        <img v-else src="https://via.placeholder.com/327x582" alt="Placeholder" />
        <figure class="post-text">
          <blockquote>
            <slot name="text" />
          </blockquote>
          <figcaption>
            <slot name="author" />
            <span v-if="slots.published_date" class="date"><slot name="published_date" /></span>
          </figcaption>
        </figure>
      </figure>
    </div>
  </div>
</template>

<script setup>
import { useSlots } from 'vue';
const slots = useSlots();
</script>

<style lang="css" scoped>
.heading-wrapper {
  padding: 15px;
  border: 1px solid #ededed;
}

.post-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 1rem;
}

.post-wrapper ::v-deep(img) {
  width: max(33%, 160px);
  object-fit: cover;
  aspect-ratio: 9/16;
}

.post-wrapper .post-text {
  flex: 1;
  padding: 1rem 0 0;
}

.post-wrapper .post-text blockquote {
  text-align: justify;
}

.post-wrapper .post-text figcaption {
  display: flex;
  align-items: center;
  justify-content: space-between;
  column-gap: 2rem;
  font-weight: bold;
  font-style: italic;
  padding-top: 2rem;
}

.post-wrapper .post-text figcaption .date {
  font-weight: 300;
  font-style: normal;
  text-align: right;
  color: darkgrey;
}

@media (min-width: 500px) {
  .post-wrapper {
    flex-direction: row;
    align-items: flex-start;
  }

  .post-wrapper .post-text {
    padding: 0 0 0 2rem;
  }
}
</style>
