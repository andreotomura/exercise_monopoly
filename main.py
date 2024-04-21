import random
import pprint # use later

# turn = complete run of the board
# match = whole game

def roll_dice():
    dice_roll = random.randrange(1, 7)       
    return dice_roll 

def impulsive(balance, price, rent): 
    return True

def demanding(balance, price, rent):
    if rent > 50:
        return True
    else:
        return False

def cautious(balance, price, rent):
    if balance - price >= 80:
        return True
    else:
        return False

def rand(balance, price, rent):
    probability = random.random()
    if probability >= 0.5:
        return True
    else:
        return False

players = {
    impulsive: {
        "position": 0,
        "balance": 300,
        "order": 0,
        "turn": 0
    },
    demanding: {
        "position": 0,
        "balance": 300,
        "order": 0,
        "turn": 0
    },
    cautious: {
        "position": 0,
        "balance": 3000,
        "turn": 0
    },
    rand: {
        "position": 0,
        "balance": 3000,
        "turn": 0
    },
}

def generate_board(slots=20):    
    board = {}
    for i in range(slots):
        owner = None
        price = random.randrange(150, 900, 50)
        rent = 0.5 /100 * price
        slot = {"owner": owner, "price": price, "rent": rent}
        board[i] = slot
    return board

def player_action(players, player, board, slot):
    slot_owner = board[slot]["owner"]
    slot_price = board[slot]["price"]
    slot_rent = board[slot]["rent"]
    player_balance = player["balance"]
    
    if slot_owner == None:
        buy_call = player(player_balance, slot_price, slot_rent)
        if buy_call == True:
            board[slot]["owner"] = player
            player["balance"] -= slot_price
    
    else:
        player["balance"] -= slot_rent
        players[slot_owner]["balance"] += slot_rent

def player_turn(player):
    
    dice_roll = roll_dice()
    player["position"] += dice_roll
    landing_slot = player["position"]
    
    player_action(landing_slot, player)

def sort_players():
    
    sorted_players = []
    valid_list = False

    while valid_list == False:
        dice_rolls = []
        for _ in range(4):
            dice_rolls.append(roll_dice())
            print(dice_rolls)
        if len(dice_rolls) == len(set(dice_rolls)):
            valid_list = True  

    players_dice_rolls = {
        "impulsive": dice_rolls[0],
        "demanding": dice_rolls[1],
        "cautious": dice_rolls[2],
        "random": dice_rolls[3],
    }

    dice_rolls.sort(reverse=True) # learn how to sort this manually later
    
    sorted_players = [player for score in dice_rolls for player, player_score in players_dice_rolls.items() if player_score == score] # ???
    print(sorted_players)
    
    for player in players:
        player["order"] = sorted_players.index(player["behavior"])

    return sorted_players


def play_turn():
    sorted_players = sort_players()

    for player in sorted_players:
        player_turn(players[sorted_players[player]]) # probably wrong







def check_balances(players): # redo!
    balances = []

    player_1_balance = players["player_1"]["balance"]
    player_2_balance = players["player_2"]["balance"]
    player_3_balance = players["player_3"]["balance"]
    player_4_balance = players["player_4"]["balance"]

    balances.append(player_1_balance)
    balances.append(player_2_balance)
    balances.append(player_3_balance)
    balances.append(player_4_balance)

    max_balance = max(balances)
    max_balance_player = balances.index(max_balance)

    print(max_balance_player)

    # for first_level_key in players.keys():
    #     print(first_level_key)
    #     for second_level_key in players[first_level_key]:
    #         print(second_level_key["balance"])

    return max(balances)



def run_game():

        

    #setup
    rounds = 0
    end_game = False
    winner = ""
    
    # loop
    for turn in range(1000):
        
        if end_game == True:
            winner = "name of the winner"
            rounds = round
            break
    
    check_balances(impulsive, demanding, cautious, random)
    end_game = True
    rounds = 1000
    winner = "who has the most balance, and tiebreak it with play order" # create an order randomly each game?

def run_program(i=300):
    for sim in range(i):
        run_game()
        print(f"Simulation nº {sim+1}")
        print("Results:")
