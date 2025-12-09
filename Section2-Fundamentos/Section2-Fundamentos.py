import pprint

# Inicio do curso
print("\n##########################################################################\n")
"""
    Docstring for Section2-Fundamentos
    Este arquivo contém exemplos básicos de código Python.    
"""

print("Ola Mundo!")

name = "Top Gun Maverick Maçarico Avião"
year = 2022
rating = 8.4

print("name", type(name))   # str
print("year", type(year))   # int
print("rating", type(rating)) # float

print(f"Filme: {name}, Ano: {year}, Avaliação: {rating}")

# try:
#     input_name = int(input("Digite seu nome: \n"))
# except ValueError:
#     input_name = input("Digite seu nome: \n")
    
# print(f"Olá, {input_name}!")

# print(f"Nome: {input_name}, Tipo: {type(input_name)}", f"Idade: {year}, Tipo: {type(year)}", sep="\n")

# Exercício 4 - Operadores
# Lê dois números inteiros
#num1 = int(input("Digite o primeiro número inteiro: \n"))
#num2 = int(input("Digite o segundo número inteiro: \n"))

# Calc""ula e imprime a soma
#print("Total", num1 + num2)

# Calcula e imprime o produto
#print("Total multiplicacao", num1 * num2)

print(name[::2])
print(name[1::2])
print(name[::-1])
print(name.lower())
print(name.upper())
print(name.title())
print(name.capitalize())
print('center ', name.center(10, '-'))
print('find ', name.find("Maverick"))

# AULA 19

filmMatrix = ["Matrix", 1999, 8.7, True]
filmPulpFiction = ["Pulp Fiction", 1994, 8.9, True]
filmsList = []

filmsList.append(filmPulpFiction)
filmsList.append(filmMatrix)
filmsList.append(filmMatrix)
print(type(filmMatrix))
print(filmMatrix)
filmsList.remove(filmMatrix)

filmsList.sort()
print("tamanho list", len(filmsList), filmsList.index(filmPulpFiction))
print("lista de filmes ", filmsList)

filmsList.clear()
print("lista de filmes ", filmsList)


#####################################
# AULA 20 - TUPLAS
#####################################

filmsTuple = ("Matrix", 1999, 8.7, True)
#filmsTuple.__add__(("Pulp Fiction", 1994, 8.9, True))
print(type(filmsTuple))
print(filmsTuple)

#####################################
# AULA 21 - SET
#####################################
print("\n########### SET #############\n")

filmsSet = {"Matrix", "Inception", "Interstellar", True, 1}
filmsSet.add("The Dark Knight")
print(type(filmsSet))

filmsSet.remove("Inception")
print(filmsSet)

###############################
# AULA 22 - DICIONÁRIOS
###############################

filmInception = {
    1: 2,
    "title": "Inception",
    "year": 2010,
    "rating": 8.8,
    "genre": ["Action", "Sci-Fi", "Thriller"]
}

print("\n########### DICIONÁRIOS #############\n")
print(type(filmInception))
print(filmInception)

print(filmInception["genre"])
print(filmInception.keys())
print(filmInception.values())
print(filmInception.items())

filmInception["director"] = "Christopher Nolan"
filmInception.update({"year": 2011})

print(filmInception)

pp = pprint.PrettyPrinter(indent=4, width=80, compact=False)
pp.pprint(filmInception)

filmsDict = {
    "inception":{
        "yearRelease": 2010,
        "imdbRating": 8.8,
        "genre": ["Sci-fi", "Action", "Thriller"]
    },
    "interstellar":{
        "yearRelease": 2014,
        "imdbRating": 8.6,
        "genre": ["Sci-fi", "Drama"]
    },
    "the dark knight":{
        "yearRelease": 2008,
        "imdbRating": 9.0,
        "genre": ["Action", "Drama", "Crime"]
    }
}


print(filmsDict["inception"]["genre"])

filmsDict["the dark knight"]["auxiliar"] = "Joseph Nolan"

pp.pprint(filmsDict)

print("\n########### Iterando Dicionários #############\n")
for film, details in filmsDict.items():
    print(f"O filme {film.title()} foi lançado em {details['yearRelease']} com avaliação {details['imdbRating']}")  


