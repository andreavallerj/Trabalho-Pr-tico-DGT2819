arquivo = open("loremipsum.txt", "r", encoding="utf-8")

conteudo_total = arquivo.read()
print(conteudo_total)
arquivo.close()

arquivo = open("loremipsum.txt", "r", encoding="utf-8")
primeira_linha = arquivo.readline()
print(primeira_linha)
arquivo.close()

arquivo = open("loremipsum.txt", "r", encoding="utf-8")
tres_caracteres = arquivo.read(3)
print(tres_caracteres)
arquivo.close()

with open("loremipsum.txt", "r", encoding="utf-8") as arquivo_with:
    conteudo_com_with = arquivo_with.read()
    print(conteudo_com_with)