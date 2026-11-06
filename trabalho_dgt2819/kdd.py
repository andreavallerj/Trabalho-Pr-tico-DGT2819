palavras = list()

with open("loremipsum.txt", "r", encoding="utf-8") as arquivo:
    # Percorre o arquivo linha a linha (Passo 3.b)
    for linha in arquivo:
        # Separa a linha em palavras utilizando o método split() (Passo 3.c)
        palavras_linha = linha.split()
        
        for palavra in palavras_linha:
          palavra_limpa = palavra.strip(".,").lower()
          if palavra_limpa:
            palavras.append(palavra_limpa)

    print(f"Total de palavras carregadas do arquivo: {len(palavras)}")

import time


inicio_tempo = time.time()

palavras.sort()

fim_tempo = time.time()
tempo_execucao = fim_tempo - inicio_tempo

print(f"Tempo de execução: {tempo_execucao:.6f} segundos")

with open("palavras_ordenadas.txt", "w", encoding="utf-8") as arquivo_saida:
    for palavra in palavras:
        arquivo_saida.write(palavra + "\n")