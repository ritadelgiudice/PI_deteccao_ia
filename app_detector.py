import re

# --- 1. Definição dos Padrões Sensíveis (Nossa "IA" simplificada) ---
# Usamos Expressões Regulares (Regex) para identificar formatos específicos.
# Estes são os "modelos" que a LGPD quer proteger.

# Dicionário de padrões e seus nomes
PADROES_SENSIVEIS = {
    # 1. CPF (Formato: XXX.XXX.XXX-XX)
    "CPF": r'\d{3}\.\d{3}\.\d{3}-\d{2}',
    
    # 2. RG (Formato: XX.XXX.XXX-X ou similar)
    "RG": r'\d{2}\.\d{3}\.\d{3}-\d{1}',
    
    # 3. Telefone/Celular (Formato: (XX) XXXXX-XXXX ou (XX) XXXX-XXXX)
    "TELEFONE": r'\(\d{2}\)\s?\d{4,5}-?\d{4}',
    
    # 4. Dados de Saúde/Religião (Simples: busca por palavras-chave)
    "SAÚDE/RELIGIÃO": r'(Católico|Evangélico|Ateu|Diabético|Alérgico|Pressão Alta)',
    
    # 5. CEP (Formato: XXXXX-XXX)
    "CEP": r'\d{5}-\d{3}'
    
    # NOTA: Endereços completos são mais complexos de capturar com Regex simples.
    # Por enquanto, focamos em identificadores fortes (CPF, RG, CEP) e palavras-chave.
}

def analisar_curriculo(caminho_arquivo):
    """
    Lê o arquivo de texto e aplica a detecção de padrões sensíveis.
    """
    print(f"--- Iniciando Análise do Arquivo: {caminho_arquivo} ---")
    
    try:
        # Abre e lê o conteúdo do arquivo
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            texto_curriculo = f.read()
    except FileNotFoundError:
        print(f"ERRO: Arquivo não encontrado em {caminho_arquivo}")
        return

    # Lista para armazenar o que foi encontrado
    dados_encontrados = {}
    total_detecções = 0

    # Itera sobre cada padrão definido
    for nome_dado, padrao_regex in PADROES_SENSIVEIS.items():
        # Usa re.findall para encontrar todas as ocorrências do padrão no texto
        ocorrencias = re.findall(padrao_regex, texto_curriculo, re.IGNORECASE)
        
        if ocorrencias:
            dados_encontrados[nome_dado] = ocorrencias
            total_detecções += len(ocorrencias)

    # --- 2. Relatório de Resultados (Segurança/LGPD) ---
    print("\n--- Relatório de Risco LGPD ---")

    if total_detecções == 0:
        print("✅ Baixo Risco: Nenhum dado sensível de formato conhecido foi detectado.")
    else:
        print(f"🚨 ALERTA DE ALTO RISCO: {total_detecções} dados sensíveis detectados!")
        print("Recomendação: Revise e remova estes dados antes de armazenar.")
        
        print("\nDetalhes das Detecções:")
        for dado, valores in dados_encontrados.items():
            # Mostra o tipo de dado encontrado e as primeiras 3 ocorrências
            print(f"- **{dado}** ({len(valores)} ocorrência(s)): {', '.join(valores[:3])}...")
            
    print("\n--- Fim da Análise ---")

# --- 3. Execução do Projeto ---
if __name__ == "__main__":
    # Chama a função principal com o nome do nosso arquivo de teste
    analisar_curriculo('curriculo_exemplo.txt')