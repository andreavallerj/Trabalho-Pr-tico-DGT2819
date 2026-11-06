arquivo_saida = open("texto.txt", "w", encoding="utf-8")

texto = list()

texto.append("Primeira linha: Lorem ipsum dolor sit amet, consectetur adipiscing elit,\n")
texto.append("Segunda linha: sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n")
texto.append("Terceira linha: Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi\n")

for frase in texto:
    arquivo_saida.write(frase)

arquivo_saida.close()