<script setup lang="ts">
import { ref } from 'vue'

const apiUrl = "http://127.0.0.1:5000";

import axios from 'axios'

const messages = ref([])

defineProps<{
  msg: string,
}>()

async function askQuery(this: any, event: any) {
  if (event.code === 'Enter') {
    const query = (<HTMLInputElement>document.getElementById("prompt-textarea")).value;
    messages.value.push({ author: "You", text: query });
    const response = await axios.post(`${apiUrl}/conversation`, { text: query });
    messages.value.push({ author: "Chatty", text: response.data });
  }
}

</script>

<template>
  <div class="greetings">
    <h1 class="green">{{ msg }}</h1>
    <h3>
      Ask me anything.
    </h3>
    <textarea id="prompt-textarea" tabindex="0" data-id="root" rows="1" placeholder="Message Chatty…" v-on:keypress="(e) => askQuery(e)"></textarea>
    <div id="chat-history">
      <div v-for="item in messages">
        <div><h3>{{ item.author }}</h3></div>
        {{ item.text }}
      </div>
    </div>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}

#prompt-textarea {
  border-color: rgb(155, 155, 155);
  width: 766px;
  height: 52px;
  border-radius: 5px;
  resize: none;
}

</style>
