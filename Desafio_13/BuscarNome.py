from idlelib.autocomplete_w import LISTUPDATE_SEQUENCE

nomes_possiveis = ["Ana", "Carlos", "Beatriz", "Daniel", "Eduardo", "Fernanda", "Gabriel", "Helena", "Luciano", "Ian"]
encontrou=False

for listar_nomes in nomes_possiveis:
    print(listar_nomes)

novo_nome = input("Informar o novo nome: ")

nomes_possiveis.append(novo_nome)

for lista_nome in nomes_possiveis:
    if novo_nome == lista_nome:
        encontrou = True

if encontrou:
    print("Achei")
else:
    print("Não achei")







