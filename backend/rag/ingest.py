from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Load documents
with open("backend/data/docs.txt", "r") as f:
    text = f.read()

# Split text
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = splitter.create_documents([text])

# Embeddings (FREE & LOCAL)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Store in Chroma
db = Chroma.from_documents(
    docs,
    embeddings,
    persist_directory="backend/chroma_db"
)

db.persist()
print("✅ Documents indexed successfully")
