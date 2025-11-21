from fastapi import FastAPI
from pydantic import BaseModel

from lmodel import LocalModel
from inpt import is_malicious_input
from otpt import is_leaking_output
from tkn import token_analyzer

app = FastAPI(title="Secure Local LLM Firewall")
model = LocalModel(model_path="models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf")

class Query(BaseModel):
    prompt: str

@app.post("/generate")
def generate(q: Query):
    prompt = q.prompt

    # Token analysis
    flags = token_analyzer(prompt)
    if flags:
        return {
            "blocked": True,
            "reason": "Obfuscated prompt attack detected",
            "flags": flags
        }

    # Malicious input filter
    if is_malicious_input(prompt):
        return {
            "blocked": True,
            "reason": "Malicious input detected"
        }
    result = model.generate(prompt)

    # Output filtering 
    if is_leaking_output(result):
        return {
            "blocked": True,
            "reason": "Unsafe model output detected",
            "raw_output": result
        }

    return {
        "blocked": False,
        "response": result
    }
