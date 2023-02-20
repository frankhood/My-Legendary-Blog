<template>
  <div class="PostDetailCmp">
    <div class="container">
      <article class="post-box">
        <header class="post-header">
          <slot name="title" />
        </header>
        <div class="post-body">
          <template v-if="!!$slots.image">
            <slot name="image" />
          </template>
          <img v-else src="https://via.placeholder.com/327x582" alt="Placeholder" />
          <div class="post-content">
            <p class="post-text">
              <slot name="text" />
            </p>
            <footer class="post-footer">
              <p>
                <slot name="author" />
                <time v-if="!!$slots.published_date" class="published-date"><slot name="published_date" /></time>
              </p>
            </footer>
          </div>
        </div>
      </article>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PostDetailCmp',
}
</script>

<style lang="css" scoped>
.post-box .post-header {
  padding: 15px;
  border: 1px solid #ededed;
}

.post-box .post-body {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 1rem;
}

.post-box .post-body ::v-deep(img) {
  width: max(33%, 160px);
  object-fit: cover;
  aspect-ratio: 9/16;
}

.post-box .post-body .post-content {
  flex: 1;
  padding: 1rem 0 0;
}

.post-box .post-body .post-content .post-text {
  text-align: justify;
}

.post-box .post-body .post-content .post-footer p {
  display: flex;
  align-items: center;
  justify-content: space-between;
  column-gap: 2rem;
  font-weight: bold;
  font-style: italic;
  padding-top: 2rem;
}

.post-box .post-body .post-content .post-footer p .published-date {
  font-weight: 300;
  font-style: normal;
  text-align: right;
  color: darkgrey;
}

@media (min-width: 500px) {
  .post-box .post-body {
    flex-direction: row;
    align-items: flex-start;
  }

  .post-box .post-body .post-content {
    padding: 0 0 0 2rem;
  }
}
</style>
