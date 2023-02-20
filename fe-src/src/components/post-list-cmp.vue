<template>
  <div class="PostListCmp">
    <div class="container">
      <div class="heading-wrapper">
        <slot name="heading" />
      </div>
      <ul class="list-wrapper">
        <slot name="list" />
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PostListCmp',
}
</script>

<style lang="css" scoped>
.heading-wrapper {
  padding: 15px;
  border: 1px solid #ededed;
}

.list-wrapper {
  list-style: none;
  margin: 0;
  padding: 0;
  border-inline: 1px solid #ededed;
}

.list-wrapper > ::v-deep(li) {
  border-bottom: 1px solid #ededed;
  padding: 15px;
}

.list-wrapper > ::v-deep(li) > a {
  color: dodgerblue;
  text-decoration: none;
}

.list-wrapper > ::v-deep(li) > a:hover {
  text-decoration: underline;
}
</style>
