# Mentor Learning Framework 🚀

An extensible and modular framework designed to transform AI assistants into specialized learning mentors, optimizing retention, reasoning, and hands-on project building.

> **Status do Projeto:** 🚧 Em Desenvolvimento (Fase Alpha)  
> **Versão Atual:** `v0.5.0 — Prompt Base Concluído`  
> **Ambiente de Destino:** Camber AI Platform & GitHub Codespaces

---

## 🎯 Missão

Construir um ecossistema agêntico modular que mude a forma como interagimos com as Inteligências Artificiais para estudar. Em vez de usar a IA para obter respostas prontas, este framework força a IA a atuar como um mentor socrático, guiando o utilizador através de analogias, desafios e validação por etapas.

---

## 🏛️ Arquitetura do Repositório

O projeto segue uma abordagem de design modular, separando as regras de comportamento (filosofia), o conhecimento técnico (personas) e a dinâmica de interação (modos):

```text
├── README.md               # Manifesto e documentação principal
├── core/                   # O DNA e princípios inegociáveis do mentor
│   └── filosofia.md        # Regras de autonomia cognitiva e ancoragem conceitual (v0.2.0)
├── personas/               # Repositório de especializações técnicas
│   └── cientista_dados.md  # Contexto e escopo do mentor de Data Science e IA (v0.3.0)
├── modos/                  # Dinâmicas de fluxo de conversação
│   └── estudo_socratico.md # Regras para o método de perguntas e respostas (v0.4.0)
└── camber_config/          # Código de infraestrutura e orquestração na nuvem
    └── main.py             # Script Python para compilar os módulos no Camber
