numeros = [42, 12, 7, 89, 23, 1, 55, 34, 19, 90, 3, 15, 68, 77, 25]
print("Numeros:", numeros)

numeros.sort()
print("Crescente:",numeros)

numeros.sort(key=None, reverse=True)
print("Decrescente:",numeros)

nomes = ["Carlos Alberto", "Ana Souza", "Bruno Lima", "Mariana Costa"]
dataNascimento = ["15/08/1995", "10/02/2001", "03/12/1988", "22/05/1999"]
cpf = ["123.456.789-01", "987.654.321-09", "456.123.789-88", "321.654.987-11"]
rg = ["MG-12.345.678", "SP-98.765.432", "RJ-11.223.344", "ES-55.667.788"]


print("\nNomes:", nomes)
nomes.sort()
print("Crescente:", nomes)
nomes.sort(reverse=True)
print("Decrescente:", nomes)

print("\nData de Nascimento:", dataNascimento)
dataNascimento.sort()
print("Crescente:", dataNascimento)
dataNascimento.sort(reverse=True)
print("Decrescente:", dataNascimento)

print("\nCPF:", cpf)
cpf.sort()
print("Crescente:", cpf)
cpf.sort(reverse=True)
print("Decrescente:", cpf)

print("\nRG:", rg)
rg.sort()
print("Crescente:", rg)
rg.sort(reverse=True)
print("Decrescente:", rg)