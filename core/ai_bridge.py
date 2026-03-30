import json
import requests

class AIBridge:
    def __init__(self, host="127.0.0.1", port="8188"):
        self.url = f"http://{host}:{port}/prompt"
    
    def ollama_prompt_generate(self, data):
        base_text = f"Rosto {data['rostos']}, olhos {data['olhos']}"
        return f"Hyper-realistc portrait, {base_text}, 8k, raw photo"
    
    def send_to_comfy(self, final_prompt):
        with open("resources/workflow_api.json", "r") as f:
            workflow = json.load(f)

        
        workflow["6"]["inputs"]["text"] = final_prompt

        payload = {"prompt": workflow}
        try:
            response = requests.post(self.url, json=payload)
            if response.status_code == 200:
                print("Execução enviada ao ComfyUI com sucesso!")
                return response.json()
        except Exception as e:
            print(f"Erro ao conectar com ComfyUI: {e}")