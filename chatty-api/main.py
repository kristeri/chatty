from flask import Flask, request, jsonify
from llm import LLM
import torch

app = Flask(__name__)

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

@app.route("/conversation", methods=["POST"])
def conversate():
    llm = LLM(DEVICE)
    query = request.get_json()
    answer = llm.ask_query(query["text"])

    return jsonify(answer), 200

if __name__ == "__main__":
    app.run(debug=False)