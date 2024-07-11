# Interpolação

template = "O saldo do %s é o total de %d" 

nome = "Maria"
saldo = 30.0

template % (nome, saldo)

type(print("OLá, %s" % 1324))
 

 # str.format {}


msg = " Olá, {} você é o player n {} e voce tem {:.3f} pontos".format("Bruno", 2, 987.3)

print(msg)

nome = "{:^11}".format("Isa")
print(nome)


nome = "{:>11}".format("Isa")
print(nome)

nome = "{:<11}".format("Isa")
print(nome)

nome = "{:#^11}".format("Isa")
print(nome)

# f-strings

nome_2 = "Isa"
texto = f"Olá, {nome_2}, seja bem vinde"

print(texto)

#unicode emoji

print("\U0001F43C")

print("\N{panda face}")

