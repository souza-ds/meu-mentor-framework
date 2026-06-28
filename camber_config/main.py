import os
def compilar_prompt_sistema():
 """
 Lê os arquivos markdown de configuração modular do framework
 e compila em uma única instrução mestre de sistema.
 """
 caminho_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
 modulos = [
 os.path.join(caminho_base, 'core', 'filosofia.md'),
 os.path.join(caminho_base, 'personas', 'cientista_dados.md'),
 os.path.join(caminho_base, 'modos', 'estudo_socratico.md')
 ]
 prompt_final = []
 for modulo in modulos:
 if os.path.exists(modulo):
 with open(modulo, 'r', encoding='utf-8') as f:
 prompt_final.append(f.read())
 else:
 print(f"Aviso: Módulo não encontrado em {modulo}")
 return "\n\n".join(prompt_final)
if __name__ == "__main__":
 prompt_mestre = compilar_prompt_sistema()
 print("=== PROMPT MESTRE COMPILADO COM SUCESSO ===")
 print(prompt_mestre[:300] + "... [Conteúdo Omitido para Visualização]")
 # Próximo passo (v0.5.0): Inicializar o agente usando a SDK do Camber
 # client = camber.Client()
 # client.agents.create(name="Mentor-DS-Socratico", system_instruction=prompt_mestre)