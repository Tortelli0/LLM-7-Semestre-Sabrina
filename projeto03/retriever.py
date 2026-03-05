from sentence_transformers import SentenceTransformer
import numpy as np

# Carregar o modelo de embeddings (ex.: all-MiniLM-L6-v2)
modelo_embeddings = SentenceTransformer('all-MiniLM-L6-v2')

# Função para gerar embeddings para o arquivo conhecimento.txt
def gerar_embeddings(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.readlines()
    
    # Gerar embeddings para cada linha
    embeddings = modelo_embeddings.encode(conteudo, convert_to_numpy=True)
    return conteudo, embeddings

# Função para encontrar as seções mais similares com base nos embeddings
def busca_por_similaridade(consulta, conteudo, embeddings):
    # Gerar o embedding da consulta
    embedding_consulta = modelo_embeddings.encode([consulta], convert_to_numpy=True)

    # Garantir que os embeddings tenham as dimensões corretas
    if embedding_consulta.ndim == 1:
        embedding_consulta = embedding_consulta.reshape(1, -1)

    if embeddings.ndim == 1:
        embeddings = embeddings.reshape(1, -1)

    # Calcular similaridades
    similaridades = np.dot(embeddings, embedding_consulta.T).flatten()

    # Ordenar por pontuação de similaridade
    indices_ordenados = np.argsort(similaridades)[::-1]

    # Retornar as seções mais relevantes
    return [conteudo[i] for i in indices_ordenados if similaridades[i] > 0.5]

# RAG Simplificado
def load_conhecimento():
    with open("projeto03/conhecimento.txt", "r", encoding="utf-8") as file:
        return file.read()
    
def simple_retriever(query, conhecimento):
    query = query.lower()
    conhecimento = conhecimento.lower()
    relevant_chunks = []
    sections = conhecimento.split("\n\n")  # Supondo que cada seção seja separada por duas quebras de linha

    for section in sections:
        if query in section:
            relevant_chunks.append(section)
    return "\n\n".join(relevant_chunks) if relevant_chunks else "Nenhuma informação relevante encontrada."