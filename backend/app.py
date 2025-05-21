from flask import Flask, request, jsonify
from utils.parse_docs import parse_document
from utils.embed_store import store_embeddings
from utils.rag_query import get_answer
from flask_cors import CORS
from langchain.schema import Document
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
UPLOAD_FOLDER = "./uploads"
vectorstore = None
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/upload", methods=["POST"])
def upload_file():
    global vectorstore
    file = request.files["file"]
    file_path = f"{UPLOAD_FOLDER}/{file.filename}"
    file.save(file_path)

    content = parse_document(file_path)
    docs = [Document(page_content=content)]
    vectorstore = store_embeddings(docs)
    print("File uploaded and processed.")
    return "File uploaded and processed."


@app.route("/query", methods=["POST"])
def query():
    data = request.get_json()
    question = data["question"]
    answer = get_answer(question, vectorstore)
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)