from controller.gerenciarCategoria import listarCategoria, inserirCategoria, editarCategoria, deletarCategoria
from controller.gerenciarAnimal import listarAnimal, inserirAnimal, editarAnimal, deletarAnimal

retorno = listarCategoria()
print(retorno)

# nome="Aves"
# #retorno = inserirCategoria(nome)

# id=4
# nome="Galinha"
# retorno = editarCategoria(id, nome)
# print(retorno)

# id = 1
# retorno = deletarCategoria(id)
# print(retorno)

# retorno = listarCategoria()
# print(retorno)

retorno = listarAnimal()
print(retorno)

# nome = "Nininha"
# idade = 2
# sexo = "Feminino"
# categoriaId = 2
# retorno = inserirAnimal(nome, sexo, idade, categoriaId)
# print(retorno)

id = 2
nome = "Dogão"
idade = 3
sexo = "Masculino"
categoriaId = 1
retorno = editarAnimal(id, nome, sexo, idade, categoriaId)



# retorno = deletarAnimal(4)
# print(retorno)


retorno = listarAnimal()
print(retorno)