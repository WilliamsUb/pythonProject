from datetime import date #import datetime module (will be used to get today's date)
from TeamPlayer import Team_Player #import TeamPlayer file

class Team:#Team class , the object of this class will hold team information
    def __init__(self, name):
        self.name = name #Setting team name
        self.players = [] #Setting up a list that will hold team players(player objects)
        self.creation_date = date.today() #Setting up date of creation of team
        self.fee_paid = False #Setting fee status
        self.team_type = 'not defined yet' #Setting team type
        self.id = 'not set yet' #Setting team id
        self.description = 'not defined yet' #Setting team description
        self.cancell_participation_date = '' #Setting team participation status
        self.fee_amount_paid = 0



    def get_team_name(self):#Defining a method to get team name
        return self.name
    def change_team_name(self, new_name):
        if new_name == self.name:
            print('new name cannot be same as old name')
            return 
        self.name = new_name
    def add_new_player(self):#Defining a method to add a player to the team
        player_name = input('Input new player name: ')
        info = input('Input player information: ')
        for player in self.players:
            if player.get_player_name() == player_name:
                print('New name cannot be same as former name')
                return
        self.players.append(Team_Player(player_name, info))
    def list_team_players(self):#Defining a method to list all players and their informtaion
        if len(self.players) == 0:
            return 'No player in this team'
        else:
            team_info = ''
            for player in self.players:
                team_info += 'Player Name: ' + player.get_player_name() + '\n'  + 'Player Information: ' + player.get_player_info() + '\n' + '\n'
            return team_info
    def list_team_player_names(self):#Defining a method to list all players names
        if len(self.players) == 0:
            return 'No players in this team'
        else:
            names = ''
            for player in self.players:
                names += player.get_player_name() + '\n'
            return names
    def remove_player(self, player_name):#Defining a method to remove player from team
        index = -10
        for player in self.players:
            if player.get_player_name() == player_name:
                index = self.players.index(player)
        if index == -10:
            print('Cannot find player')
        else:
            self.players.pop(index)
    def change_player_name(self, old_name, new_name):#Defining a method to change player name
        for player in self.players:
            if player.get_player_name() == old_name:
                player.change_player_name(new_name)
                return
        print('Not found')
        return
    def change_player_info(self, player_name, new_info):#Defining a method to change player information
        for player in self.players:
            if player.get_player_name() == player_name:
                player.change_player_info(new_info)
                return
        print('Not found')
        return
    def get_player_info(self, player_name):#Defining a method to get player information based on player name
        for player in self.players:
            if player.get_player_name() == player_name:
                return player.get_player_info()
        return 'Not found'
    def update_fee_status(self, status):#Defining a method to upate fee status
        self.fee_paid = status
    def define_team_type(self, t_type):#Defining a method to set team type (boys or girls)
        self.team_type = t_type
    def set_id(self, given_id):#Defining a method to set team id
        self.id = given_id
    def get_id(self):
        return self.id
    def show_fee_status(self):#Defining a method to show fee status
        return self.fee_paid
    def show_team_type(self):#Defining a method to show team type
        if self.team_type == 'not defined yet':
            return 'type not defined yet'
        return self.team_type
    def show_team_id(self):#Defining a method to show team id
        if self.id == 'NOT AVAILABLE':
            return 'ID NOT AVAILABLE'
        return self.id
    def set_team_description(self, description):#Defining a method to set team description
        self.description = description
    def show_team_info(self):#Defining a method to show team information
        if len(self.players) == 0:
            return 'No players added to the team yet'
        info = 'team id : {}'.format(self.id) + '\n'
        info += 'team name : {}'.format(self.name) + '\n'
        info += 'created : {}'.format(self.creation_date) + '\n'
        info += 'fee status : {}'.format(self.fee_paid) + '\n'
        info += 'team type : {}'.format(self.team_type) + '\n'
        info += 'fee amount paid : {}'.format(self.fee_amount_paid) + '\n'
        if len(self.cancell_participation_date) == 0:
            info += 'participation status : Participating' + '\n'
        elif len(self.cancell_participation_date) > 0:
            info += 'participation status : Participation cancelled on {}'.format(self.cancell_participation_date) + '\n'
        info += 'team description : {}'.format(self.description) + '\n'
        info += self.list_team_players()
        return info
    def cancell_participation(self, date_of_cancellation):#Defining a method to change team's participation status
        self.cancell_participation_date = date_of_cancellation
    def show_participation_status(self):#Defining a method to show team's participation status
        if len(self.cancell_participation_date) == 0:
            return 'Team is participating'
        elif len(self.cancell_participation_date) > 0:
            return 'Team cancelled participation on {}'.format(self.cancell_participation_date)
    def show_fee_paid_amount(self):
        return self.fee_amount_paid
    def change_fee_paid_amount(self, amount):
        self.fee_amount_paid = amount
        self.fee_paid = True