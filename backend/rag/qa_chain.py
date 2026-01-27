# from langchain_community.vectorstores import Chroma
# from langchain_community.embeddings import HuggingFaceEmbeddings

# from backend.prompts.few_shot import FEW_SHOT_PROMPT
# from langchain_community.llms import Ollama

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
from backend.prompts.few_shot import FEW_SHOT_PROMPT
from langchain.chains import RetrievalQA
# from langchain.chains.retrieval_qa.base import RetrievalQA


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory="backend/chroma_db",
    embedding_function=embeddings
)

llm = Ollama(model="mistral")

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=db.as_retriever(),
    chain_type_kwargs={
        "prompt": FEW_SHOT_PROMPT
    }
)
