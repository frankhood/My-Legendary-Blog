<template>
  <div class="PostListAsyncCmp">
    <div class="container">
      <div class="heading-wrapper">
        <slot name="heading" />
        <span class="items-number">Numero di post: {{ itemsNumber }}</span>
      </div>
      <ul class="list-wrapper">
        <li
          v-for="item in apiResponse"
          :key="`item-${item.slug}-${_uid}`"
        >
          <a :href="item.url">{{ item.title }}</a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'PostListAsyncCmp',
  props: {
    dataApiUrl: {
      type: String,
      required: true,
    }
  },
  data() {
    return {
      apiResponse: [],
    }
  },
  computed: {
    itemsNumber() {
      return this.apiResponse.length;
    }
  },
  mounted() {
    axios.get(this.dataApiUrl).then((response) => {
      this.apiResponse = response.data;
    }).catch((err) => {
      console.log('Error: ', err);
    });
  }
}
</script>

<style lang="css" scoped>
.heading-wrapper {
  padding: 15px;
  border: 1px solid #ededed;
}

.heading-wrapper .items-number {
  display: block;
  font-weight: 300;
  font-style: normal;
  text-align: center;
  color: darkgrey;
  padding-top: 10px;
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
