# Interpolação

template = "O saldo do %s é o total de %d" 

nome = "Maria"
saldo = 30.0

template % (nome, saldo)

type(print("OLá, %s" % 1324))
 

 # New style


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


