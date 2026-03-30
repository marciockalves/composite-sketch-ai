# Variáveis de ambiente
PYTHON := uv run python
UV := uv
APP_ENTRY := app.py
OUTPUT_DIR := ./core/output_images

.PHONY: help install run clean test dev-env

help: ## Mostra os comandos disponíveis
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Instala as dependências usando o uv
	@echo "Instalando dependências com uv..."
	$(UV) sync

run: ## Executa o Wizard do Retrato Falado
	@echo "Iniciando a interface PySide6..."
	$(PYTHON) $(APP_ENTRY)

dev-env: ## Prepara o ambiente de desenvolvimento (pastas necessárias)
	@echo "Criando estrutura de diretórios..."
	mkdir -p core/output_images resources wizard
	@echo "Ambiente pronto."

clean: ## Limpa arquivos temporários do Python e imagens de cache
	@echo "Limpando arquivos __pycache__ e outputs..."
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf $(OUTPUT_DIR)/*.png
	@echo "Limpeza concluída."

check-server: ## Verifica se o Ollama e o ComfyUI estão respondendo
	@echo "Verificando Ollama (11434)..."
	@curl -s -I http://localhost:11434 > /dev/null && echo "Ollama: OK" || echo "Ollama: OFFLINE"
	@echo "Verificando ComfyUI (8188)..."
	@curl -s -I http://localhost:8188 > /dev/null && echo "ComfyUI: OK" || echo "ComfyUI: OFFLINE"

# Novas variáveis para o Docker
DOCKER_COMPOSE := docker compose

.PHONY: up down status logs pull-model

up: ## Sobe os serviços da IA (Ollama + WebUI) em background
	@echo "Subindo containers de IA..."
	$(DOCKER_COMPOSE) up -d
	@echo "Serviços iniciados. Ollama na porta 11434 e WebUI na 3000."

down: ## Para e remove os containers de IA
	@echo "Parando serviços..."
	$(DOCKER_COMPOSE) down
	@echo "Serviços finalizados."

status: ## Verifica o status dos containers e uso da GPU
	$(DOCKER_COMPOSE) ps
	@docker exec -it ollama nvidia-smi || echo "GPU não detectada no container."

logs: ## Mostra os logs do Ollama em tempo real
	$(DOCKER_COMPOSE) logs -f ollama

pull-model: ## Garante que o modelo llama3.1 está baixado
	@echo "Solicitando pull do modelo llama3.1..."
	docker exec -it ollama ollama pull llama3.1