
from llama_cpp import Llama

class LocalModel:
    def __init__(self, model_path: str):
        self.llm = Llama(
            model_path=model_path,
            n_ctx=4096,
            n_threads=8,
            verbose=False
        )

    def generate(self, prompt: str, max_tokens: int = 256) -> str:
        output = self.llm(
            prompt,
            max_tokens=max_tokens,
            temperature=0.7,
            stop=["<|eot|>"]
        )

        return output["choices"][0]["text"].strip()
