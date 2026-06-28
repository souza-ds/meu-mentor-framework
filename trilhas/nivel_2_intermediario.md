# 🔵 NÍVEL 2 — INTERMEDIÁRIO

## Bloco 07 — Estatística Avançada + AB Testing
### Conteúdo Teórico
- Testes Paramétricos: Shapiro-Wilk, Chi-Square Test, ANOVA, MANOVA.
- Não-Paramétricos: Mann-Whitney U Test, Wilcoxon Signed-Rank.
- Avançado: Estatística Bayesiana.
### Prática & Execução
- Codespaces: Simulação de experimentos A/B com dados sintéticos via SciPy/Statsmodels. Salvar em `bloco-07-estatistica-avancada/`.
### 🧩 Mini projeto do Bloco 07
**Framework de A/B Test (Python):** Notebook que gera dados de conversão (controle vs variação), calcula tamanho amostral, executa teste estatístico (z-test/chi-square) e fecha com recomendação de negócio (ship/no-ship).

## Bloco 08 — Econometria & Séries Temporais
### Conteúdo Teórico
- Conceitos: Stationarity em Séries Temporais, Decomposição.
- Modelagem: Time Series Analysis com ARIMA, Forecasting com Prophet.
### Prática & Execução
- Kaggle: Time Series.
- Codespaces: Usar dados de vendas ou clima para predição. Subir para `bloco-08-series-temporais/`.
### 🧩 Mini projeto do Bloco 08
**Forecast de Demanda:** Decomposição da série de tempo, baseline ingênuo vs ARIMA/Prophet, avaliação com MAE/MAPE e gráficos com intervalos de confiança.

## Bloco 09 — Feature Engineering
### Conteúdo Teórico
- Detecção: Outliers com Z-Score e IQR.
- Transformações: Scaling, Normalização, Label Encoding, One-Hot Encoding, SMOTE (Dados desbalanceados).
- Seleção: Feature Selection com Scikit-Learn, Redução de Dimensionalidade (PCA).
### Prática & Execução
- Kaggle: Feature Engineering.
- Codespaces: Aplicar 4 técnicas em dataset misto e enviar para `bloco-09-feature-engineering/`.
### 🧩 Mini projeto do Bloco 09
**Feature Store "Caseira":** Estruturar uma pasta `features/` com funções reutilizáveis de engenharia de dados e testar o impacto em dois modelos diferentes usando o mesmo pipeline.

## Bloco 10 — ML Avançado (XGBoost, SHAP, Otimização)
### Conteúdo Teórico
- Boosting: Gradient Boosting, XGBoost, LightGBM, CatBoost, Ensemble (Stacking/Blending).
- XAI & Otimização: Hyperparameter Tuning com Optuna, Pipelines do Scikit-Learn, SHAP Values (Interpretabilidade).
### Prática & Execução
- Kaggle: Intermediate ML e Machine Learning Explainability.
- Codespaces: Executar pipeline Optuna + SHAP em competição tabular. Salvar em `bloco-10-ml-avancado/`.
### 🧩 Mini projeto do Bloco 10
**Tuning + Interpretabilidade:** Otimizar um modelo com Optuna, extrair SHAP values globais e locais e escrever um resumo executivo explicando quais variáveis importam para o negócio.

## Bloco 11 — Streamlit + FastAPI (Deploy Simples)
### Conteúdo Teórico
- Frontend: Streamlit Tutorial (Construção de Apps de Dados).
- Backend: FastAPI (Deploy de modelos como API REST), Pydantic (Validação de schemas).
- Infra: Pickle/Joblib para serialização, python-dotenv para variáveis de ambiente.
### Prática & Execução
- Documentações oficiais do Streamlit e FastAPI.
- Codespaces: Criar API local para o modelo do Nível 1. Salvar em `bloco-11-streamlit-fastapi/`.
### 🧩 Mini projeto do Bloco 11
**API + UI Integrados:** Servir um modelo via FastAPI (endpoint `/predict`) com validação Pydantic e consumi-lo em uma interface Streamlit amigável.

---
### 🏆 Projeto Final Nível 2 — Portfólio com Deploy
**Previsão de Preço de Imóveis — App Streamlit + API FastAPI**
Dataset: House Prices (Kaggle) -> Limpeza -> Feature Engineering robusta -> Otimização de XGBoost/LightGBM via Optuna -> Integração de gráficos SHAP explicativos no app Streamlit -> Deploy público no Streamlit Cloud ou Railway.
