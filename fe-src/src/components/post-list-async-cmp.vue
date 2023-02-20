<template>
  <div class="PostListAsyncCmp">
    <div class="container">
      <div class="heading-wrapper">
        <slot name="heading" />
      </div>
      <ul class="list-wrapper">
        <li
          v-for="item in listItems"
          :key="`item-${item.slug}-${_uid}`"
        >
          <span
            v-if="item.apiError"
            class="api-error"
          >
            {{ item.apiError }}
          </span>
          <a
            v-else
            :href="item.url"
          >
            {{ item.title }}
          </a>
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
    listItems() {
      if (this.apiResponse.length > 0) {
        if (!this.apiResponse.some(el => el.apiError)){
          return this.apiResponse.filter(el => el.url);
        }
      }

      return this.apiResponse;
    }
  },
  mounted() {
    new Promise((resolve, reject) => {
      axios.get(this.dataApiUrl).then((response) => {
        this.apiResponse = response.data;
        resolve(response.data);
      }).catch((err) => {
        this.apiResponse.push({ apiError: 'Something wrong with the API' });
        reject(err);
      });
    });
  }
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

.list-wrapper > ::v-deep(li) > .api-error {
  color: red;
}

.list-wrapper > ::v-deep(li) > a {
  color: dodgerblue;
  text-decoration: none;
}

.list-wrapper > ::v-deep(li) > a:hover {
  text-decoration: underline;
}
</style>
