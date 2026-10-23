import random


# ==========================================
# Classe PlayerId : représente un joueur
# ==========================================

class PlayerId:
    def __init__(self, username, turn_position, statut="inGame"):
        self.user = username
        self.order = turn_position
        self.stat = statut
        self.positionX = 0  # Position de départ, avant la case 1

    def lancer_de(self):
        return random.randint(1, 6)

    def avancer(self, de):
        self.positionX += de

    def __str__(self):
        return (
            f"{self.user} | Position : {self.positionX} "
            f"| Statut : {self.stat}"
        )


# ==========================================
# Classe CreateGame : crée les joueurs
# ==========================================

class CreateGame:
    @staticmethod
    def initiate_user(n):
        players = {}

        for i in range(n):
            username = input(f"Nom du joueur {i + 1} : ")

            while not username.strip():
                username = input("Le nom ne peut pas être vide : ")

            players[username] = PlayerId(username, i)

        return players


# ==========================================
# Classe BasePlate : représente le plateau
# ==========================================

class BasePlate:
    def __init__(self):
        self.plate = [0] * 63

    def move_player(self, player, de):
        player.avancer(de)

        # Le joueur ne peut pas dépasser la case 63
        if player.positionX >= 63:
            player.positionX = 63
            player.stat = "winner"

    def display(self, players):
        print("\n--- État du plateau ---")

        for player in players.values():
            print(player)

        print("-----------------------")


# ==========================================
# Classe GameHandler : gère la partie
# ==========================================

class GameHandler:
    def __init__(self):
        self.players = {}
        self.plateau = BasePlate()

    def start_game(self):
        print("================================")
        print("       JEU DE L'OIE")
        print("================================")

        # Demander le nombre de joueurs
        while True:
            try:
                n = int(input("Nombre de joueurs : "))

                if n >= 2:
                    break

                print("Il faut au moins 2 joueurs.")

            except ValueError:
                print("Veuillez saisir un nombre entier.")

        # Créer les joueurs
        self.players = CreateGame.initiate_user(n)

        print("\nLa partie commence !")

        # Boucle principale : un tour après l'autre
        while True:
            for player in self.players.values():

                print(f"\nAu tour de {player.user} !")
                input("Appuyez sur Entrée pour lancer le dé...")

                de = player.lancer_de()
                print(f"{player.user} obtient un {de}.")

                self.plateau.move_player(player, de)

                print(
                    f"{player.user} avance jusqu'à "
                    f"la case {player.positionX}."
                )

                # Vérifier si le joueur a gagné
                if player.stat == "winner":
                    print("\n================================")
                    print(f"🏆 {player.user} a gagné la partie !")
                    print("================================")

                    self.plateau.display(self.players)
                    return

            # Afficher les positions à la fin de chaque tour complet
            self.plateau.display(self.players)
