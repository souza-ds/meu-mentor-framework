# 🟣 NÍVEL 3 — AVANÇADO

## Bloco 12 — Deep Learning
### Conteúdo Teórico
- Fundamentos: Redes Neurais Artificiais, Backpropagation.
- Arquiteturas: CNN (Convolucionais), RNN (Recorrentes), LSTM.
### Prática & Execução
- Kaggle: Intro to Deep Learning e Computer Vision.
- Codespaces: Executar fine-tuning de modelos pré-treinados da Hugging Face. Salvar em `bloco-12-deep-learning/`.
### 🧩 Mini projeto do Bloco 12
**Fine-tuning de Classificação (Hugging Face):** Pipeline de treinamento de um transformer pequeno, avaliação detalhada com F1-Score/Accuracy, análise de matriz de confusão e inferência local.

## Bloco 13 — Engenharia de Dados Básica
### Conteúdo Teórico
- Ingestão: Consumo de APIs REST com Python, manipulação de arquivos Parquet, Integração com PostgreSQL via SQLAlchemy.
- Pipelines: Conceitos de Processo ETL, Introdução ao Apache Airflow e dbt (Data Build Tool).
### Prática & Execução
- Comunidade: Módulos iniciais do Data Engineering Zoomcamp (DataTalks.Club).
- Codespaces: Montar pipeline API -> Parquet -> Postgres. Salvar em `bloco-13-engenharia-de-dados/`.
### 🧩 Mini projeto do Bloco 13
**ETL Incremental Real:** Script que consome dados incrementais de uma API, aplica checagens de qualidade de schema/nulos, salva localmente em Parquet e persiste no Postgres, gerando logs de erro.

## Bloco 14 — Big Data & Processamento Distribuído
### Conteúdo Teórico
- Batch: Ecossistema Apache Hadoop, Engenharia de Computação Distribuída com Apache Spark (PySpark).
- Streaming: Conceitos de mensageria assíncrona com Apache Kafka.
### Prática & Execução
- Ambiente: Databricks Community Edition (Gratuito) + Módulo Spark do Data Engineering Zoomcamp. Salvar códigos em `bloco-14-big-data/`.
### 🧩 Mini projeto do Bloco 14
**Migração Pandas -> Spark:** Processar um dataset volumoso aplicando as mesmas transformações em Pandas e PySpark, comparando tempo de execução, consumo de memória e explicando a mudança de paradigma do processamento distribuído.

## Bloco 15 — Docker + Cloud Básica
### Conteúdo Teórico
- Containers: Dockerfile, Docker Compose, Containerização de aplicações Python e Modelos de Machine Learning.
- DevOps & Cloud: CI/CD Pipelines com GitHub Actions, Introdução a Clouds Públicas (AWS e GCP).
### Prática & Execução
- Plataformas: Google Cloud Skills Boost e guias Docker. Containerizar o projeto do Nível 2. Salvar em `bloco-15-docker-cloud/`.
### 🧩 Mini projeto do Bloco 15
**Docker + CI/CD Mínimo:** Criar o Dockerfile e docker-compose para uma API FastAPI e estruturar um workflow do GitHub Actions que roda testes automatizados unitários a cada push.

---
### 🏆 Projeto Final Nível 3 — Portfólio End-to-End
**Pipeline de Detecção de Fraude End-to-End (Batch) com Monitoramento**
Ingestão de dados públicos -> Armazenamento em banco PostgreSQL -> Transformação e modelagem de tabelas usando dbt -> Modelo preditivo de classificação (XGBoost/LightGBM) -> API FastAPI empacotada em container Docker -> Deploy no Railway/Cloud Run -> Monitoramento de data drift e performance de modelo usando a biblioteca Evidently AI.
