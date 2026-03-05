# Responsável por conectar com a API

from openai import OpenAI
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

class LLMClient:
    def __init__(self, provider="openai", model="gpt-4o-mini"):
        self.provider = provider
        self.model = model

        if provider == "openai":
            self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            self.model = os.getenv("OPENAI_MODEL", model)

            # Validar se o modelo especificado é válido
            if not self.model:
                raise ValueError("Erro: O modelo especificado no .env (OPENAI_MODEL) é inválido ou não foi definido.")
        elif provider == "groq":
            self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
            self.model = os.getenv("GROQ_MODEL", model)

            # Validar se o modelo especificado é válido
            if not self.model:
                raise ValueError("Erro: O modelo especificado no .env (GROQ_MODEL) é inválido ou não foi definido.")
        else:
            raise ValueError("Provider não suportado: {provider}")


    def generate_text(self, system_prompt, user_prompt, temperature=0.2):
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        if self.provider == "openai":
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature
            )
            return response.choices[0].message.content.strip()
        
        elif self.provider == "groq":
            # Implementação para o provider Groq
            try:
                # Usar o método 'chat' para gerar respostas
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    temperature=temperature
                )

                # Ajustar para acessar o conteúdo corretamente
                return response.choices[0].message.content.strip()
            except Exception as e:
                raise RuntimeError(f"Erro ao utilizar o provider Groq: {e}")