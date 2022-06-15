import random

from pokemon import *

NOMES = ["Joshua", "Ricardo", "Paty", "Laerte", "Mille", "Ash", "Gary", "Jimmy", "Toby", "Jan", "Suzane", "Diogo",
             "Karol", "Mino", "Bloom", "Pierre", "Jessie", "James"]

POKEMONS = [
    PokemonFogo("Charmander"), PokemonFogo("Ninetales"), PokemonFogo("Slugma"), PokemonFogo("Oricorio"),
    PokemonAgua("Squirtle"), PokemonAgua("Seadra"), PokemonAgua("Huntail"), PokemonAgua("Poliwag"),
    PokemonPsi("Gothita"), PokemonPsi("Abra"), PokemonPsi("Chingling"), PokemonPsi("Hypno"),
    PokemonEletrico("Pikachu"), PokemonEletrico("Tynamo"), PokemonEletrico("Manectric"), PokemonEletrico("Morpeko"),
    PokemonLutador("Lucario"), PokemonLutador("Pancham"), PokemonLutador("Falinks"), PokemonLutador("Marshadow")
]


class Pessoa:

    def __init__(self, nome=None, pokemons=[], dinheiro=100):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

        self.dinheiro = dinheiro

    def __str__(self):
        return self.nome

    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print("{} escolheu {}".format(self, pokemon_escolhido))
            return pokemon_escolhido
        else:
            print("Esse jogador não possui nenhum pokemon para ser escolhido :(")

    def mostrar_pokemons(self):
        if self.pokemons:
            print("Pókemons de {}:".format(self))
            for index, pokemon in enumerate(self.pokemons):
                print("{} - {}".format(index, pokemon))
        else:
            print("Não há pókemons no inventário... ainda")

    def mostrar_dinheiro(self):
        print("Você possui $ {}".format(self.dinheiro))

    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print("Você recebeu $ {}".format(quantidade))
        self.mostrar_dinheiro()

    def batalhar(self, pessoa):
        print("{} iniciou uma batalha {}".format(self, pessoa))

        pessoa.mostrar_pokemons()
        pokemon_inimigo = pessoa.escolher_pokemon()

        pokemon = self.escolher_pokemon()

        if pokemon and pokemon_inimigo:
            while True:
                vitoria = pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print("{} venceu a batalha.".format(self))
                    self.ganhar_dinheiro(pokemon_inimigo.level * 100)
                    break
                vitoria_inimiga = pokemon_inimigo.atacar(pokemon)
                if vitoria_inimiga:
                    print("{} venceu a batalha.".format(pessoa))
                    break

        else:
            print("Essa batalha não pode acontecer.")

class Player(Pessoa):
    tipo = "player"

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print("{} capturou {}!".format(self, pokemon))

    def escolher_pokemon(self):
        self.mostrar_pokemons()

        if self.pokemons:
            while True:
                escolha = input("Escolha seu pokemon!\n")
                try:
                    escolha = int(escolha)
                    pokemon_escolhido = self.pokemons[escolha]
                    print("{}, eu escolho você!".format(pokemon_escolhido))
                    return pokemon_escolhido
                except:
                    print("Escolha inválida")
        else:
            print("Esse jogador não possui nenhum pokemon para ser escolhido :(")


    def explorar(self):
        if random.random() <= 0.2:
            pokemon = random.choice(POKEMONS)
            print("Um pokemon selvagem apareceu: {}".format(pokemon))

            escolha = input("Deseja capturá-lo? (s/n) \n")

            if escolha == "s":
                if random.random() >= 0.5:
                    self.capturar(pokemon)
                else:
                    print("{} fugiu! Que pena...".format(pokemon))
            else:
                print("Ok, boa viagem!")

        else:
            print("Essa exploração não resultou em nada...")


class Inimigo(Pessoa):
    tipo = "inimigo"

    def __init__(self, nome=None, pokemons=None):
        if not pokemons:
            inimigo_aleatorio = []
            for i in range(random.randint(1, 6)):
                inimigo_aleatorio.append(random.choice(POKEMONS))

            super().__init__(nome=nome, pokemons=inimigo_aleatorio)
        else:
            super().__init__(nome=nome, pokemons=pokemons)
