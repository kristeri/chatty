# Chatty
Chatty is a proof of concept AI conversation application using Meta's LLaMA model on the backend with a client interface inspired by OpenAI's ChatGPT. The app uses Vue.js on the frontend and python on the backend with a Flask API. The LLM used is Meta's open source LLaMA 2.

# Installation

# Backend

Download the llama-2-7b-chat.ggmlv3.q4_0.bin model and place it under chatty-api folder. Notice that this model is quite large (3.79 GB).

https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/blob/main/llama-2-7b-chat.ggmlv3.q4_0.bin

Install python and C++ development tools provided by Microsoft visual studio.

https://visualstudio.microsoft.com/free-developer-offers/

Select Python development -> check Python native development tools.

Select Desktop development with C++.

Install Nvidia CUDA to run the model on GPU.

https://developer.nvidia.com/cuda-downloads

Upgrade setup tools.

pip install --upgrade setuptools

Install torch with CUDA support.

```
pip install --force-reinstall --no-cache-dir torch --index-url https://download.pytorch.org/whl/cu118
```

Install llama-cpp-python

```
set CMAKE_ARGS="-DLLAMA_CUBLAS=on" && set FORCE_CMAKE=1 && pip install --verbose --force-reinstall --no-cache-dir llama-cpp-python==0.1.78
```


Navigate to the API directory.

```
cd chatty-api
```

Install dependencies.

```
pip install -r requirements.txt
```

Run the Flask API, the backend app runs on port http://localhost:5000/

```
python main.py
```

# Frontend

Make sure the API is running correctly for proper Chatbot testing.

Navigate to the UI directory.

```
cd chatty-ui
```

Install the dependencies

```
npm install
```

Run the app

```
npm run dev
```

The frontend app is accessible on http://localhost:5173/