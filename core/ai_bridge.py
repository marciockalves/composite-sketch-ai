import json
import requests

class AIBridge:
    def __init__(self, host="127.0.0.1", port="8188"):
        self.url = f"http://{host}:{port}/prompt"
    
    def ollama_prompt_generate(self, data):
        base_text = f"Rosto {data['rosto']}, olhos {data['olhos']}"
        return f"Hyper-realistc portrait, {base_text}, 8k, raw photo"
    
    def send_to_comfy(self, final_prompt):
        pass