from Team import Team  # Importing team module to use class Team
from random import randrange  # Importing random number generator
import time
from TeamPlayer import Team_Player #Importing team player module to use Class Team player


class U_I:  # Class User Interaction with menu input, an object of this class will hold teams
    def __init__(self):
        self.team_ids = []  # list to hold team ids
        self.teams = []  #  list to hold team objects
        self.team_ids_mappings = {}  # Setting up a dictionary that maps team ids to team objects
        self.team_ids_names_mappings = {}  # a dictionary that maps team ids to team names

    def create_team(self, team_name):  # Defining a method to create a team with unique id
        if team_name in self.teams:
            print('Team already exists!')  # Checking if the team being created already exists
            return
        id = randrange(1000, 10000)
        while True:
            if id not in self.team_ids:
                break
            else:
                id = randrange(1000, 10000)  # Setting random id for the team being created
        self.team_ids.append(id)
        new_team = Team(team_name)  # Creating new team object
        print('CONGRATULATIONS!! YOUR TEAM', {team_name}, 'AS BEEN CREATED\n' 'GOOD JOB!')
        print('Add players to the team!\n')
        for _ in range(1):  # Adding 11 new players to the team created
            new_team.add_new_player()
        self.teams.append(new_team)  # Appending newly created team to list that contains all teams
        self.team_ids_mappings[id] = new_team  # Mapping newly created team object to the team id
        self.team_ids_names_mappings[id] = new_team.get_team_name()  # Mapping newly created team id to the team name
        new_team.set_id(id)  # Setting up team id of newly created team

    def edit_team(self, team_id):  # Defining a method to enable editing a team
        if team_id not in self.team_ids:
            print('TEAM ID NOT FOUND! \n')  # If team id is not found return not found error
            return
        team = self.team_ids_mappings[team_id]  # Finding  team using id
        while True:  # Options that use method to do listed tasks
            c = int(input('Choose an options \n '
                          '1: List team players \n '
                          '2: Remove a player \n '
                          '3: Change player name \n '
                          '4: Change player information \n '
                          '5: Update fee status \n '
                          '6: Define team type \n '
                          '7: Set team description \n '
                          '8: Add player \n'
                          '9: Cancell team participation \n '
                          '10: Change team name \n '
                          '11: Update fee paid amount \n '
                          '12: Back to main menu \n'
                          '---------------------------\n '
                          'Enter an Option: '))
            if c == 1:
                print(team.list_team_player_names())
            elif c == 2:
                name = input('Enter player name: ')
                team.remove_player(name)
            elif c == 3:
                old = input('Enter old name: ')
                new = input('Enter new name: ')
                team.change_player_name(old, new)
            elif c == 4:
                name = input('Enter player name: ')
                info = input('Enter information: ')
                team.change_player_info(name, info)
            elif c == 5:
                status = input('Enter fee status(True or False): ')
                if status == 'True' or status == 't' or status == 'true' or status == 'T':
                    status = True
                elif status == 'False' or status == 'f' or status == 'false' or status == 'F':
                    status = False
                team.update_fee_status(status)
            elif c == 6:
                type_of_team = input('Enter team type(boys or girls): ')
                team.define_team_type(type_of_team)
            elif c == 7:
                desc = input('Enter description: ')
                team.set_team_description(desc)
            elif c == 8:
                team.add_new_player()
            elif c == 9:
                date = input('Enter participation cancellation date in YYYY-MM-DD format: ')
                team.cancell_participation(date)
            elif c == 10:
                new_name = input('Enter new name: ')
                teamid = team.get_id()
                team.change_team_name(new_name)
                self.team_ids_names_mappings.pop(teamid)
                self.team_ids_names_mappings[teamid] = new_name
            elif c == 11:
                amount = input('Enter paid amount: ')
                team.change_fee_paid_amount(amount)
            elif c == 12:
                break
            else:
                print('Invalid choice, try again\n')

    def show_teams_ids(self):  # Defining a method to show team ids
        if len(self.team_ids_names_mappings) == 0:  # Return not found msg if no teams exist
            return 'No teams registered yet'
        teams_and_ids = ''
        for team_id, team_name in self.team_ids_names_mappings.items():  # Find teams by their ids
            teams_and_ids += 'id : {} | name : {} \n'.format(team_id, team_name)
        return teams_and_ids

    def show_team_info(self, unique_id):  # Defining a method to show team information using team ID
        if unique_id not in self.team_ids_mappings:  # Return not found msg if no teams exist
            return 'No teams registered yet'
        for team_id in self.team_ids_mappings:  # Find team by ID and get it's information
            if team_id == unique_id:
                return self.team_ids_mappings[team_id].show_team_info()

    def delete_team(self, unique_id):  # Defining a method to delete team
        if len(self.teams) == 0:
            print('No teams registered yet')  # Return not found msg if no teams exist
            return
        if unique_id not in self.team_ids_mappings:
            print('Team does not exist')
            return
        self.team_ids.remove(unique_id)  # Remove teams from all lists containing team's information
        self.team_ids_mappings.pop(unique_id)
        self.team_ids_names_mappings.pop(unique_id)
        for team in self.teams:
            if team.show_team_id() == unique_id:
                self.teams.remove(team)
                break

    def list_all_teams(self):
        if len(self.teams) == 0:
            return 'No teams registered yet'
        teams = ''
        for t in self.teams:  # List all teams by names
            teams += t.get_team_name() + '\n'
        return teams

    def list_all_boys_teams(self):  # Defining a method to list all boys teams names
        if len(self.teams) == 0:
            return 'No teams registered yet'  # Return not found msg if no teams exist
        teams = ''
        for t in self.teams:
            if t.show_team_type() == 'boys':  # List all boys teams by names
                teams += t.get_team_name() + '\n'
        return teams

    def list_all_girls_teams(self):  # Defining a method to list all girls teams names
        if len(self.teams) == 0:
            return 'No teams registered yet'  # Return not found msg if no teams exist
        teams = ''
        for t in self.teams:
            if t.show_team_type() == 'girls':  # List all girls teams by names
                teams += t.get_team_name() + '\n'
        return teams

    def get_percent_of_teams_that_paid_fee(self):  # Defining a method to get percentage of teams that paid fee
        if len(self.teams) == 0:
            return 'No teams registered yet'  # Return not found msg if no teams exist
        num_of_total_teams = len(self.teams)
        print('Total number of teams: {}'.format(num_of_total_teams))
        fee_paid = 0
        for curr_team in self.teams:
            if curr_team.show_fee_status() == True:
                fee_paid += 1
        return 'Percentage of teams that have paid fee: {}'.format(
            (fee_paid / num_of_total_teams) * 100)  # finding percentage of teams that paid the fee

    def get_all_teams_data(self):  # Defining a method to get all teams data
        if len(self.team_ids) == 0:
            return 'No teams registered yet'  # Return not found msg if no teams exist
        data = ''
        for id in self.team_ids:
            data += self.show_team_info(id) + '\n\n'  # Accumlating data of all teams
        return data


print('HELLO!!')
menu = U_I()  # Instance of U_I class
choice = 0
while choice != 1 or choice != 2 or choice != 3 or choice != 4 or choice != 5 or choice != 6 or choice != 7 or choice != 8 or choice != 9 or choice != 10: #To prevent wrong choice
    try:
        #main menu option
        choice = int(input('===========Main menu===============\n'
                           '--------Select an option------------\n '
                           '1: Create new team \n '
                           '2: Edit team \n '
                           '3: Show team information \n '
                           '4: Update fields for a team \n '
                           '5: Delete team \n '
                           '6: List all teams names \n '
                           '7: List boys/girls teams names\n '
                           '8: Show percentage of teams that paid fee \n '
                           '9: Show all teams information \n'
                           '10:Exit \n'
                           '==================================\n '
                           'Enter Option {main menu}: '))


      
      
      #User inputs for main menu
        if choice == 1:
            team_name = input('Insert team name: ')
            menu.create_team(team_name)
            print('Team', menu.show_teams_ids())

        elif choice == 2:
            team_id = int(input('Insert team id :'))
            menu.edit_team(team_id)
        elif choice == 3:
            team_id = int(input('Insert team id: '))
            print(menu.show_team_info(team_id))
        elif choice == 4:
            team_id = int(input('Insert team id: '))
            menu.edit_team(team_id)
        elif choice == 5:
            team_id = int(input('Enter team id: '))
            menu.delete_team(team_id)
        elif choice == 6:
            print(menu.list_all_teams())
        elif choice == 7:
            type_of_team = input('Enter type of team (boys or girls): ')
            if type_of_team == 'boys':
                print(menu.list_all_boys_teams())
            elif type_of_team == 'girls':
                print(menu.list_all_girls_teams())
        elif choice == 8:
            print(menu.get_percent_of_teams_that_paid_fee())
        elif choice == 9:
            data = menu.get_all_teams_data()
            print(data)

        elif choice == 10:
            print('Goodbye!!!')
            break
    except:
            print('Invalid choice, try again \n')


