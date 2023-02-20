import { createApp } from 'vue';
import './assets/css/common.css';
import PostListCmp from './components/post-list-cmp.vue';
import PostListAsyncCmp from './components/post-list-async-cmp.vue';
import PostDetailCmp from './components/post-detail-cmp.vue';

const app = createApp({});
app.component('post-list-cmp', PostListCmp);
app.component('post-list-async-cmp', PostListAsyncCmp);
app.component('post-detail-cmp', PostDetailCmp);
app.mount('#app');
