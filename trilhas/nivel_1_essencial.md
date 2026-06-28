# 🟢 NÍVEL 1 — ESSENCIAL

## Bloco 01 — Python Fundamentals + Git/GitHub
### Conteúdo Teórico (GeeksforGeeks)
- Noções Básicas: Variáveis, Tipos de Dados, Operadores, Entrada e Saída (input/print), Condicionais (if/else), Loops.
- Funções: Estruturadas, Funções Lambda, *args e **kwargs.
- Estruturas de Dados: Strings, Listas, Dicionários, Tuplas, Sets.
- Python Avançado: Módulos e Imports, Tratamento de Exceções, Comprehensions, map/filter/zip/enumerate, Geradores e yield, Orientação a Objetos (OOP).
- Arquivos e I/O: Manipulação de CSV/JSON, Context Managers (with), Módulo datetime.
- Git e GitHub: Commit, Push, Pull, Branching, Merge, README.
### Prática & Execução
- Kaggle: Python Course.
- Codespaces: Desenvolver scripts locais e dar push para a branch `bloco-01-python/`.
### 🧩 Mini projeto do Bloco 01
**CLI de Organização de Estudos (Python):** Script que lê um CSV/JSON de tarefas de estudo (título, bloco, status), permite filtrar por status/bloco e exporta um relatório simples em Markdown para o repositório.

## Bloco 02 — SQL + Bancos de Dados
### Conteúdo Teórico
- Fundamentos: SELECT, WHERE, GROUP BY, ORDER BY, Agregações, JOINs (INNER, LEFT, RIGHT, FULL).
- SQL Avançado: Subqueries, Window Functions, CTEs (Common Table Expressions).
### Prática & Execução
- Kaggle: Intro to SQL e Advanced SQL.
- Codespaces: Conectar a um SQLite local e salvar em `bloco-02-sql/`.
### 🧩 Mini projeto do Bloco 02
**Banco de Estudos + Consultas (SQLite):** Modele um banco SQLite com tabelas (`estudos`, `topicos`, `progresso`) e escreva queries para listar progresso por bloco, calcular % concluído e identificar tópicos atrasados.

## Bloco 03 — Matemática & Estatística Básica
### Conteúdo Teórico
- Visão Geral: Maths & Statistics for Data Science.
- Descritiva e Probabilidade: Estatística Descritiva, Distribuições de Probabilidade, Teorema de Bayes.
- Inferencial: Hypothesis Testing, T-test, Z-test.
### Prática & Execução
- Codespaces: Prática direta em Python usando NumPy/SciPy/Statsmodels em datasets reais da UCI/Kaggle. Salvar em `bloco-03-matematica-estatistica/`.
### 🧩 Mini projeto do Bloco 03
**Relatório Estatístico (NumPy/SciPy):** Dataset real com estatísticas descritivas, correlações interpretadas em texto e 2 testes de hipótese (ex: t-test) com conclusão simples.

## Bloco 04 — Pandas, NumPy + Limpeza de Dados
### Conteúdo Teórico
- Core: NumPy e Pandas Step-by-Step.
- Carregamento: CSV, Excel, JSON, SQL para DataFrame, Web Scraping com BeautifulSoup.
- Limpeza: Dados Faltantes, Removendo Duplicatas, GroupBy, Data Preprocessing para ML, Large Datasets com Pandas.
### Prática & Execução
- Kaggle: Pandas e Data Cleaning.
- Codespaces: Limpar um dataset sujo do Kaggle e salvar em `bloco-04-pandas-numpy/`.
### 🧩 Mini projeto do Bloco 04
**Pipeline de Limpeza Reutilizável (Pandas):** Script/Notebook que recebe um CSV cru e aplica padronização de colunas, tratamento de missing, remoção de duplicatas e validações de faixas de valores.

## Bloco 05 — Visualização de Dados + EDA
### Conteúdo Teórico
- EDA: Exploratory Data Analysis, Análise Univariada/Bivariada/Multivariada, Correlação.
- Matplotlib: Line, Bar, Histogram, Heatmap, Box Plot, Scatter Plot.
- Avançado: Seaborn (Pair Plot) e Plotly Interativo.
### Prática & Execução
- Kaggle: Data Visualization.
- Codespaces: EDA completa enviada para `bloco-05-eda-visualizacao/`.
### 🧩 Mini projeto do Bloco 05
**EDA Storytelling (Matplotlib/Seaborn):** Fazer uma análise exploratória focada em narrativa contendo 5 insights visuais, validação de hipóteses e recomendações de próximos passos.

## Bloco 06 — Machine Learning Fundamental
### Conteúdo Teórico
- Fundamentos: ML Pipeline, Scikit-Learn Guide, Underfitting/Overfitting, Bias vs Variance, Cross Validation, Métricas de Avaliação.
- Algoritmos: Regressão Linear, Regressão Logística, Árvore de Decisão, Random Forest, KNN, SVM, Naive Bayes.
### Prática & Execução
- Kaggle: Intro to Machine Learning e Intermediate Machine Learning.
- Codespaces: Treinar modelos no Titanic/House Prices e subir para `bloco-06-machine-learning/`.
### 🧩 Mini projeto do Bloco 06
**Baseline vs Modelo Melhor (scikit-learn):** Escolher um dataset, criar um baseline simples, aplicar melhorias (features/algoritmo) e comparar métricas explicando o trade-off.

---
### 🏆 Projeto Final Nível 1 — Portfólio para Estágio
**Churn de Clientes (Telco) — EDA + Modelo + Storytelling**
Dataset: Telco Customer Churn (Kaggle) -> Limpeza -> EDA completa -> Modelo de classificação (baseline vs melhor) -> Análise de erros e trade-offs (precision/recall) -> Repositório estruturado com README profissional.
