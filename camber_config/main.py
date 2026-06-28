import os
import json

def descobrir_arquivo_nivel(bloco_atual):
    bloco = str(bloco_atual).lower()
    if any(b in bloco for b in ['01', '02', '03', '04', '05', '06']):
        return 'nivel_1_essencial.md'
    elif any(b in bloco for b in ['07', '08', '09', '10', '11']):
        return 'nivel_2_intermediario.md'
    elif any(b in bloco for b in ['12', '13', '14', '15']):
        return 'nivel_3_avancado.md'
    else:
        return 'especializacoes.md'

def compilar_prompt_mestre():
    projeto_raiz = os.path.dirname(os.path.abspath(__file__))
    caminho_progresso = os.path.join(projeto_raiz, 'progresso.json')
    
    bloco_atual = "Bloco 01"
    topico_atual = "Variáveis e Tipos de Dados"
    aluno = "Estudante"
    
    if os.path.exists(caminho_progresso):
        with open(caminho_progresso, 'r', encoding='utf-8') as f:
            progresso = json.load(f)
            bloco_atual = progresso.get('bloco_atual', 'Bloco 01')
            topico_atual = progresso.get('topico_atual', 'Variáveis e Tipos de Dados')
            aluno = progresso.get('aluno', 'Estudante')

    arquivo_nivel = descobrir_arquivo_nivel(bloco_atual)
    
    modulos = [
        os.path.join(projeto_raiz, 'core', 'filosofia.md'),
        os.path.join(projeto_raiz, 'personas', 'cientista_dados.md'),
        os.path.join(projeto_raiz, 'trilhas', 'index.md'),
        os.path.join(projeto_raiz, 'trilhas', arquivo_nivel),
        os.path.join(projeto_raiz, 'modos', 'estudo_socratico.md')
    ]
    
    prompt_final = ""
    for modulo in modulos:
        if os.path.exists(modulo):
            with open(modulo, 'r', encoding='utf-8') as f:
                prompt_final += f.read() + "\n\n"
            
    contexto_dinamico = f"""
# 📍 CONTEXTO EM TEMPO REAL DA SESSÃO (NÃO IGNORAR)
Você está atendendo o estudante: **{aluno}**.
Ele está exatamente neste ponto do mapa de estudos:
- **Bloco Atual:** {bloco_atual}
- **Tópico Atual:** {topico_atual}

Sua missão é iniciar a conversa saudando o aluno e trazendo o primeiro desafio prático/teórico deste tópico específico.

Quando você validar que o aluno concluiu com sucesso todas as 3 camadas deste tópico (Teoria, Prática e Execução com Commit), você deve encerrar a sua resposta gerando obrigatoriamente a seguinte tag de comando no final do texto:
`[ACTION: CONCLUIDO | BLOCO: {bloco_atual} | TOPICO: {topico_atual}]`
"""
    prompt_final += contexto_dinamico

    caminho_saida = os.path.join(projeto_raiz, 'prompt_camber_final.md')
    with open(caminho_saida, 'w', encoding='utf-8') as f:
        f.write(prompt_final)
        
    print("\n🔥 PROMPT MESTRE COMPILADO COM SUCESSO!")
    print(f"💾 Copie o conteúdo de: 'prompt_camber_final.md' e cole no Camber.\n")

if __name__ == "__main__":
    compilar_prompt_mestre()
