class Team_Player:  # Player class , the object of this class will hold player information

    def __init__(self, player_name, info):
        self.player_name = player_name  # Setting player name
        self.playerinfo = info  # Setting player information

    def get_player_name(self):  # Defining a method that will return player name
        return self.player_name

    def get_player_info(self):  # Defining a method that will return player information
        return self.playerinfo

    def change_player_name(self, new_name):  # Defining a method that can change player name
        self.player_name = new_name

    def change_player_info(self, new_info):  # Defining a method that can change player information
        self.playerinfo = new_info
