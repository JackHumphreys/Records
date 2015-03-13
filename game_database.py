import pickle

class GameData:
    def __init__(self):
        self.name = None
        self.platform = None
        self.genre = None
        self.cost = None
        self.players = None
        self.online = None

def load_games():
    with open("U:\git\Records\gamefile.txt", mode = "rb") as gamefile:
        file_data = pickle.load(gamefile)
        print(file_data[0].name)
              
            

def save_games(games, record):
    with open("U:\git\Records\gamefile.txt", mode = "ab") as gamefile:
        for record in games:
            pickle.dump(games, gamefile)
            


#the parameter is games because eventually you will be displaying
#multiple games using this function
def display_games(games, record):
    print()
    print()
    print("|{0:^20}|{1:^5}|{2:^5}|{3:^6}|{4:^5}|{5:^5}|".format("Name", "Platform", "Genre", "Cost", "Players", "Online"))
    print("-"*59)
    for record in games:
        print("|{0:^20}|{1:^8}|{2:^5}|{3:^5}|{4:^7}|{5:^6}|".format(record.name, record.platform, record.genre, record.cost, record.players, record.online))
        print("-"*59)
        
def get_game_from_user():
    gameslist = []
    finished = False
    while not finished:
        tempRecord = GameData()
        name = input("Name of game (-1 to finish): ")
        if name == "-1":
            finished = True
        else:
            tempRecord.name = name
            tempRecord.platform = input("Platform: ")
            tempRecord.genre = input("Genre: ")
            tempRecord.cost = input("Cost (£): ")
            tempRecord.players = input("Number of players: ")
            tempRecord.online = input("Online (Y or N): ")
            gameslist.append(tempRecord)
    return gameslist, tempRecord

    

def display_menu():
    print()
    print("***Welcome to the Computer and Video Game Database***")
    print()
    print("1. Add new games")
    print("2. Display games")
    print("3. Exit program")
    print()



def main():
    load_games()
    exit_program = False
    while not exit_program:
        display_menu()
        selected_option = int(input("Please select a menu option: "))
        if selected_option == 1:
            games, record = get_game_from_user()
        elif selected_option == 2:
            display_games(games, record)
        elif selected_option == 3:
            save_games(games, record)
        else:
            print("Please enter a valid option (1-3)")
            print()

if __name__ == "__main__":
    main()



