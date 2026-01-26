from fastapi import FastAPI
from pydantic import BaseModel
from backend.rag.qa_chain import qa_chain


app = FastAPI()

class Question(BaseModel):
    query: str

@app.post("/ask")
def ask_question(question: Question):
    response = qa_chain.run(question.query)
    return {
        "result": response
    }
