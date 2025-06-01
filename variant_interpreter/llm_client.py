from langchain_ollama import OllamaLLM

# Initialize the Ollama deepseek model (make sure Ollama server is running locally)
llm = OllamaLLM(model="deepseek-r1")

def interpret_variants(text: str) -> str:
    """
    Send variant data text to the deepseek model and get interpretation.
    """
    prompt = f"Interpret these genomic variants:\n{text}"
    response = llm.invoke(prompt)
    return response
