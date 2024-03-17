<script setup lang="ts">
import { ref } from 'vue'

const apiUrl = "http://127.0.0.1:5000";

import axios from 'axios'

const messages = ref([]);
let showLoading = ref(false);

defineProps<{
  msg: string,
}>()

async function askQuery(this: any, event: any) {
  if (event.code === 'Enter') {
    event.preventDefault();
    const textArea = <HTMLInputElement>document.getElementById("prompt-textarea");
    const query = textArea.value;
    textArea.value = "";
    messages.value.push({ author: "You", text: query });
    showLoading.value = true;
    axios.post(`${apiUrl}/conversation`, { text: query }).then(response => {
      messages.value.push({ author: "Chatty", text: response.data });
      showLoading.value = false;
    })
  }
}

</script>

<template>
  <div class="greetings">
    <h1 class="green">{{ msg }}</h1>
    <h3>
      Ask me anything.
    </h3>
    <div v-show="showLoading">
      <div class="dot-flashing"></div>
    </div>
    <textarea id="prompt-textarea" tabindex="0" data-id="root" rows="1" placeholder="Message Chatty…" v-on:keypress="(e) => askQuery(e)"></textarea>
    <div id="chat-history">
      <div v-for="item in messages">
        <div><p class="author-text">{{ item.author }}</p class="author-text"></div>
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
  margin-bottom: 12px;
}

.greetings {
  overflow-y: auto
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

.author-text {
  font-weight: bold;
}

#prompt-textarea {
  border-color: rgb(155, 155, 155);
  width: 766px;
  height: 52px;
  border-radius: 15px;
  resize: none;
  padding: 10px;
}

.dot-flashing {
  margin: 0px auto;
  margin-top: 10px;
  margin-bottom: 10px;
  position: relative;
  width: 10px;
  height: 10px;
  border-radius: 5px;
  background-color: hsla(160, 100%, 37%, 1);
  color: hsla(160, 100%, 37%, 1);
  animation: dot-flashing 1s infinite linear alternate;
  animation-delay: 0.5s;
}
.dot-flashing::before, .dot-flashing::after {
  content: "";
  display: inline-block;
  position: absolute;
  top: 0;
}
.dot-flashing::before {
  left: -15px;
  width: 10px;
  height: 10px;
  border-radius: 5px;
  background-color: hsla(160, 100%, 37%, 1);
  color: hsla(160, 100%, 37%, 1);
  animation: dot-flashing 1s infinite alternate;
  animation-delay: 0s;
}
.dot-flashing::after {
  left: 15px;
  width: 10px;
  height: 10px;
  border-radius: 5px;
  background-color: hsla(160, 100%, 37%, 1);
  color: hsla(160, 100%, 37%, 1);
  animation: dot-flashing 1s infinite alternate;
  animation-delay: 1s;
}

@keyframes dot-flashing {
  0% {
    background-color: hsla(160, 100%, 37%, 1);
  }
  50%, 100% {
    background-color: rgba(152, 128, 255, 0.2);
  }
}

</style>
