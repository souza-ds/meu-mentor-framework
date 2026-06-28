# 🚀 TRILHAS DE ESPECIALIZAÇÃO (PÓS-NÍVEL 2)

## 🌐 ESPECIALIZAÇÃO: MLOps (Machine Learning Operations)

### Bloco MLOps-01 — Versionamento de Dados e Modelos
- Teoria: Conceito de MLOps, Tracking de experimentos com MLflow, Versionamento de bases de dados com DVC (Data Version Control).
- Prática: Curso "Made With ML" de MLOps. Tracking de 5 runs com hiperparâmetros diferentes salvando os artefatos visuais e arquivos pickle.
- 🧩 **Mini projeto:** Comparação de experimentos automatizada gerando relatório de melhor run no MLflow. Subir para `trilha-mlops/`.

### Bloco MLOps-02 — Pipelines de ML em Produção
- Teoria: Orquestradores de pipelines (Kubeflow), arquitetura de Feature Stores, Integração Contínua para Modelos de ML (CT - Continuous Training).
- Prática: MLOps Specialization (Duke University). Criar automação de treino via GitHub Actions.
- 🧩 **Mini projeto:** Pipeline de retreino acionado por alteração de dados que roda testes de validação de modelo e gera um novo release do arquivo final.

### Bloco MLOps-03 — Monitoramento e Model Drift
- Teoria: Diferença entre Data Drift e Concept Drift, métricas de estabilidade de população (PSI), monitoramento de modelos em produção.
- Prática: Documentação oficial do Evidently AI.
- 🧩 **Mini projeto:** Relatório de monitoramento simulando dados reais de produção vs dados de validação usando Evidently, gerando alertas estruturados quando o drift ultrapassar o limite aceitável de 10%.

---

## 🤖 ESPECIALIZAÇÃO: AI Engineering (IA Generativa)

### Bloco AI-01 — LLMs e Engenharia de Prompts
- Teoria: Fundamentos de LLMs (Large Language Models), IA Generativa, Padrões de escrita de prompts (Zero-shot, Few-shot, Chain-of-Thought), Ecossistema Hugging Face.
- Prática: Kaggle AI Ethics + Cursos rápidos da DeepLearning.AI. Chamar APIs gratuitas do Groq/Gemini no Codespaces.
- 🧩 **Mini projeto:** Playground de testes que roda 10 variações de prompts em 20 inputs distintos, medindo a taxa de alucinação, latência e consistência do formato JSON de saída. Subir para `trilha-ai-engineering/`.

### Bloco AI-02 — RAG (Retrieval-Augmented Generation)
- Teoria: Arquitetura RAG para bases de conhecimento externas, Tokenização, Text Chunking, Embeddings e Bancos de Dados Vetoriais (Chroma/Pinecone), Framework LangChain.
- Prática: Cursos de RAG da DeepLearning.AI e documentação oficial do LangChain.
- 🧩 **Mini projeto:** Mecanismo RAG funcional que processa arquivos PDF acadêmicos, divide em blocos textuais corretos, indexa localmente e responde dúvidas do usuário citando os trechos exatos de origem.

### Bloco AI-03 — Agentes de IA
- Teoria: Conceito de Agentic AI, Sistemas Multi-Agentes, Atribuição de ferramentas (*Tools*), Tomada de decisão autonôma em malha fechada, Orquestração de grafos de estados com LangGraph.
- Prática: AI Agents in LangGraph (DeepLearning.AI).
- 🧩 **Mini projeto:** Agente autônomo construído em LangGraph equipado com ferramentas nativas de busca na internet, calculadora e leitor de arquivos, capaz de encadear ações para resolver um problema complexo com logs de execução.

---
### 🏆 Projeto Final AI Engineering
**Assistente de Estudos com RAG + Agente + Deploy**
Interface onde o usuário faz o upload de PDFs -> Pipeline extrai texto e indexa embeddings no banco vetorial Chroma -> Agente conversacional desenvolvido em LangGraph interage mantendo memória de curto/longo prazo e respondendo consultas com base nas fontes -> Interface web desenvolvida em Streamlit -> Deploy público integrado no Railway.
