from langchain.prompts import PromptTemplate

FEW_SHOT_PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are an AI assistant that answers questions using retrieved documents.

Example:
Q: How do I integrate authentication?
A:
{{
  "summary": "Authentication is done via middleware",
  "steps": ["Add middleware", "Validate tokens"],
  "confidence": "High"
}}

Now answer the user question using the same JSON format.

Context:
{context}

Question: {question}
Answer:
"""
)
