# meu-mentor-framework

# Mentor Learning Framework 🚀

An extensible and modular framework designed to transform AI assistants into specialized learning mentors, optimizing retention, reasoning, and hands-on project building.

> **Status do Projeto:** 🚧 Em Desenvolvimento (Fase Alpha)  
> **Versão Atual:** `v0.1.0 — Estrutura Inicial`  
> **Ambiente de Destino:** Camber AI Platform & GitHub Codespaces

---

## 🎯 Missão

Construir um ecossistema agêntico modular que mude a forma como interagimos com as Inteligências Artificiais para estudar. Em vez de usar a IA para obter respostas prontas, este framework força a IA a atuar como um mentor socrático, guiando o utilizador através de analogias, desafios e validação por etapas.

O primeiro domínio de aplicação prático é **Ciência de Dados e Inteligência Artificial**, mas a arquitetura foi desenhada para ser agnóstica e expandir-se para qualquer área do conhecimento.
---

## 🏛️ Arquitetura do Repositório

O projeto segue uma abordagem de design modular, separando as regras de comportamento (filosofia), o conhecimento técnico (personas) e a dinâmica de interação (modos):

```text
├── README.md               # Manifesto e documentação principal
├── core/                   # O DNA e princípios inegociáveis do mentor
│   └── filosofia.md        # Regras de autonomia cognitiva e ancoragem conceitual
├── personas/               # Repositório de especializações técnicas
│   └── cientista_dados.md  # Contexto e escopo do mentor de Data Science e IA
├── modos/                  # Dinâmicas de fluxo de conversação
│   └── estudo_socratico.md # Regras para o método de perguntas e respostas
└── camber_config/          # Código de infraestrutura e orquestração na nuvem
    └── main.py             # Script Python para compilar os módulos no Camber
