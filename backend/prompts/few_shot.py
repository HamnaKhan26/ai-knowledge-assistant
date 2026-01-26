FEW_SHOT_PROMPT = """
You are an AI assistant that answers questions using retrieved documents.

Example:
Q: How do I integrate authentication?
A:
{
  "summary": "Authentication is done via middleware",
  "steps": ["Add middleware", "Validate tokens"],
  "confidence": "High"
}

Now answer the user question using the same JSON format.
"""
