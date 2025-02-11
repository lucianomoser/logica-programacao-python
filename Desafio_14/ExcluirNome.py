nomes_possiveis = [
    "Ana", "Carlos", "Beatriz", "Daniel", "Eduardo", "Fernanda", "Gabriel", "Helena", "Luiz", "Mariana",
    "Luiz", "Sofia", "Larissa", "Isabela", "Ricardo", "Julia", "Marcelo", "Larissa", "Felipe", "Ana"
]


nova_lista_nomes = []

for nome_atual in nomes_possiveis:
        if nome_atual not in nova_lista_nomes:
            nova_lista_nomes.append(nome_atual)

for nome_excluido in nova_lista_nomes:
    print(nome_excluido)









