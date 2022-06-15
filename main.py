import pickle
from pokemon import *
from pessoa import *


def escolher_pokemon_inicial(player):
    print("{}, você poderá escolher agora o pokemon que irá te acompanhar nesta jornada!".format(player))

    pikachu = PokemonEletrico("Pikachu", level=1)
    charmander = PokemonFogo("Charmander", level=1)
    squirtle = PokemonAgua("Squirtle", level=1)

    print("Você tem essas 3 opções: ")
    print("1. ", pikachu)
    print("2. ", charmander)
    print("3. ", squirtle)

    while True:
        escolha = input("Escolha seu pokemon!\n")

        if escolha == "1":
            player.capturar(pikachu)
            break
        elif escolha == "2":
            player.capturar(charmander)
            break
        elif escolha == "3":
            player.capturar(squirtle)
            break
        else:
            print("Escolha inválida")

def salvar_jogo(player):
    try:
        with open("database.db", "wb") as arquivo:
            pickle.dump(player, arquivo)
            print("Jogo salvo com sucesso!")
    except Exception as error:
        print("Erro ao salvar jogo")
        print(error)

def carregar_jogo():
    try:
        with open("database.db", "rb") as arquivo:
            player = pickle.load(arquivo)
            print("Loading feito com sucesso!")
            return player
    except Exception as error:
        print("Save não encontrado, essa deve ser sua primeira vez aqui!")


if __name__ == "__main__":
    print("\n-------------------------------------------")
    print("Bem vindo ao jogo de Pokemon de terminal :D")
    print("-------------------------------------------\n")

    player = carregar_jogo()

    if not player:
        nome = input("Qual é o seu nome?\n")
        player = Player(nome)
        print("Olá ,{}, aqui quem fala é o prof. Carvalho.".format(nome))
        print("Este é um mundo habitado por criaturas chamadas de pokemon, minha função é estudá-las.")
        print("O seu objetivo a partir de hoje é se tornar um mestre pokemon, capturando os pokemons e treinando-os!")
        print("Você encontrará inimigos no caminho, lute com eles.")
        player.mostrar_dinheiro()

        if player.pokemons:
            print("Já vi que você tem alguns pokemons...")
            player.mostrar_pokemons()

        else:
            print("Pelo visto você ainda não tem nenhum pokemon, então precisa escolher um!")
            escolher_pokemon_inicial(player)

        print("Pronto! Agora que você já possui um pokemon, enfrente seu maior arqui-inimigo de infância, o Garry (meu netinho)")
        gary = Inimigo(nome="Gary", pokemons=[PokemonAgua("Squirtle", level=1)])
        player.batalhar(gary)
        salvar_jogo(player)

    while True:
        print("O que deseja fazer agora?")
        print("1. Explorar mundo")
        print("2. Lutar com inimigo")
        print("3. Checar Pokeagenda")
        print("0. Sair do jogo")
        escolha = input("Sua escolha:\n")

        if escolha == "0":
            print("Fechando o jogo...")
            break
        elif escolha == "1":
            player.explorar()
            salvar_jogo(player)
        elif escolha == "2":
            inimigo = Inimigo()
            player.batalhar(inimigo)
            salvar_jogo(player)
        elif escolha == "3":
            player.mostrar_pokemons(player)
        else:
            print("Escolha inválida!")
