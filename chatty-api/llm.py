import sys, time, torch, numpy

from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.base import BaseCallbackHandler
from langchain.chains import LLMChain
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import LlamaCpp
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter

class LLM(BaseCallbackHandler):
  def __init__(self, device):
    self.tokenstring = ""
    self.device = device

  def on_llm_new_token(self, token, **kwargs) -> None:
    self.tokenstring += token

  def ask_query(self, query):
    print("Device used for LLM: %s" % self.device)
    start = time.time()
    
    print("Loading Callback Manager")
    LLMout = LLM(self.device)
    
    print("Loading embeddings")
    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2", model_kwargs={"device": self.device})
    
    print("Loading LlamaCpp")
    llm = LlamaCpp(model_path = "llama-2-7b-chat.ggmlv3.q8_0.bin", 
                   n_ctx = 2048,
                   n_gpu_layers = 100,
                   n_batch = 512,
                   n_threads = 1,
                   top_k = 10000,
                   temperature = 0.7,
                   max_tokens = 4096,
                   callback_manager = CallbackManager([LLMout]), verbose = False)
    print("Setup took %d seconds" % round(time.time() - start, 2))
    
    template = """'{text}'"""
    prompt = PromptTemplate(template = template, input_variables = ["text"])
    chain = LLMChain(llm = llm, prompt = prompt, verbose = False)
    
    # Run the chain
    chain.run(text = query)
    print("Response after %d seconds" % round(time.time() - start, 2))

    return LLMout.tokenstring
