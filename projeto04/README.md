# Projeto 04 - Assistente com Memória

Chatbot conversacional com memória persistente, persona definida, limite de histórico e funções Python integradas.

---

## Como executar

### Pré-requisitos

- Python 3.9+
- Conta e chave de API Groq (gratuita em [console.groq.com](https://console.groq.com))

### Instalação

```bash
cd projeto04
pip install -r requirements.txt
```

### Configuração

Crie um arquivo `.env` na raiz do workspace (ou dentro de `projeto04/`) com:

```
GROQ_API_KEY=sua_chave_aqui
GROQ_MODEL=llama-3.1-8b-instant
```

### Execução

```bash
python main.py
```

---

## Funcionalidades implementadas

| Parte | Funcionalidade | Detalhe |
|-------|---------------|---------|
| 1 | Comando `/limpar` | Apaga o histórico de conversa e retorna "Memória da conversa apagada." |
| 2 | Persona do assistente | Mensagem de sistema define um assistente educado, objetivo e levemente bem-humorado |
| 3 | Limite de memória | Mantém no máximo as últimas 10 mensagens; as mais antigas são descartadas automaticamente |
| 4 | Funções Python integradas | **Calcular idade** (dado "nasci em YYYY-MM-DD ou DD/MM/YYYY") e **converter temperatura** (ex.: "37C para F") |
| 5 | Persistência de dados | Histórico salvo em `history.json` e carregado automaticamente ao reiniciar o programa |

### Exemplos de uso das funções

```
Você: Qual minha idade se nasci em 1998-07-15?
Assistente: A idade é 27 anos (nascido em 1998-07-15).

Você: Converter 100C para F
Assistente: 100.0°C = 212.0°F

Você: /limpar
Assistente: Memória da conversa apagada.
```

---

## Reflexão

### Se o histórico crescer muito, quais problemas podem ocorrer no uso de LLMs?

O principal problema é o limite de contexto (context window) do modelo: cada requisição envia todo o histórico acumulado, e os modelos têm um número máximo de tokens que conseguem processar de uma vez. Ultrapassar esse limite causa erros ou truncamento silencioso das mensagens mais antigas, fazendo o assistente "esquecer" partes da conversa sem avisar. Além disso, históricos grandes aumentam o custo de cada chamada (cobrado por token) e a latência das respostas, já que o modelo precisa processar mais texto a cada turno.

### Por que algumas tarefas são melhores resolvidas por funções Python do que pelo próprio LLM?

LLMs são modelos probabilísticos: eles estimam a resposta mais provável com base em padrões do treinamento, mas não executam cálculos de forma determinística. Operações como calcular uma idade exata a partir de uma data de nascimento, converter temperaturas com precisão de ponto flutuante ou gerar uma senha criptograficamente segura exigem exatidão absoluta e resultados reproduzíveis — algo que funções Python garantem. O LLM pode errar por arredondamento, confundir datas ou simplesmente alucinar um resultado plausível porém errado. Delegar esse tipo de tarefa a código Python garante correção, testabilidade e velocidade.

### Quais riscos existem ao deixar que o LLM tome decisões sobre quando usar uma função?

Quando o LLM decide sozinho chamar (ou não) uma função, surgem três riscos principais:

1. **Falsos positivos**: o modelo pode acionar uma função em contextos inadequados, produzindo respostas fora de lugar (ex.: detectar "temperatura" em uma conversa sobre clima emocional e tentar converter um número inexistente).
2. **Falsos negativos**: o modelo pode deixar de chamar a função e tentar calcular por conta própria, introduzindo erros silenciosos que o usuário dificilmente percebe.
3. **Injeção de prompt**: um usuário mal-intencionado pode redigir mensagens que enganam o LLM para executar funções com parâmetros não esperados, especialmente se as funções tiverem efeitos colaterais (escrita em disco, chamadas externas etc.). Por isso é importante validar as entradas antes de passá-las para qualquer função, independentemente de quem acionou a chamada.

---

## Dificuldades encontradas

- **Compatibilidade de API**: a biblioteca `openai` possui dois estilos de chamada distintos (Chat Completions e Responses API). O Groq suporta apenas o padrão Chat Completions (`client.chat.completions.create`), e usar o método errado resulta em erro 404 silencioso.
- **Detecção de intenção sem LLM de roteamento**: implementar a lógica de detecção por regex é frágil para linguagem natural variada. Uma arquitetura mais robusta usaria o próprio LLM para classificar intenções (function calling / tool use), mas isso aumenta a complexidade e o custo por chamada.
- **Persistência entre sessões**: garantir que a mensagem de sistema não seja duplicada ao recarregar o JSON exigiu verificação explícita no `load_history`.
