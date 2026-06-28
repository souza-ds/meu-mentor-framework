import json
import os

def atualizar_progresso_estudos(bloco: str, topico: str, status: str = "concluido") -> str:
    """
    Registra de forma autônoma que o aluno concluiu um tópico ou bloco específico no arquivo progresso.json.
    Chame esta função SEMPRE que validar que o aluno executou o exercício prático com sucesso.
    """
    arquivo_json = "progresso.json"
    
    # 1. Se o arquivo não existir, cria um esqueleto básico
    if not os.path.exists(arquivo_json):
        dados = {
            "aluno": "Estudante de IA",
            "bloco_atual": bloco,
            "topico_atual": topico,
            "historico_concluido": []
        }
    else:
        # 2. Se já existir, lê os dados atuais
        with open(arquivo_json, "r", encoding="utf-8") as f:
            dados = json.load(f)
            
    # 3. Atualiza o estado atual do aluno
    dados["bloco_atual"] = bloco
    dados["topico_atual"] = topico
    
    # 4. Adiciona ao histórico de concluídos se já não estiver lá
    registro = f"{bloco}: {topico}"
    if registro not in dados["historico_concluido"]:
        dados["historico_concluido"].append(registro)
        
    # 5. Salva de volta no arquivo json
    with open(arquivo_json, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
        
    return f"Sucesso: O progresso do aluno foi atualizado. {registro} marcado como {status}."
