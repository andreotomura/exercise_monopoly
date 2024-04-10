import random

# def pretty_print_dict(dict): # https://www.geeksforgeeks.org/python-pretty-print-a-dictionary-with-dictionary-value/
#     pretty_dict = ''
#     for k, v in dict.items():
#         pretty_dict += f'{k}: \n'
#         for value in v:
#             pretty_dict += f'   {value}: {v[value]}\n'
#     print(pretty_dict)
#     return

players = [
    #0
    {
        "behavior": "impulsive",
        "position": 0,
        "balance": 300,
        "order": None
    },
    #1
    {
        "behavior": "demanding",
        "position": 0,
        "balance": 300,
        "order": None
    },
    #2
    {
        "behavior": "cautious",
        "position": 0,
        "balance": 300,
        "order": None
    },
    #3
    {
        "behavior": "random",
        "position": 0,
        "balance": 300,
        "order": None
    },
]

def generate_board(slots=20):
    
    board = []
    
    for _ in range(slots):
        owner = ''
        price = random.randrange(150, 900, 50)
        rent = 0.5 /100 * price
        slot = {"owner": owner, "price": price, "rent": rent}

        # {
        #     "owner": "PLAYER X",
        #     "price": 1_000.00,
        #     "rent": 5
        # }

        board.append(slot)
    
    # test
    # print(board)

    return board

board = generate_board()

def roll_dice():
    
    dice_roll = random.randrange(1, 6)
    
    # teste
    # print(dice_roll)
    
    return dice_roll 

def buy_decision(slot_price, slot_rent, player):
    
    if player["balance"] >= slot_price:
        match player["behavior"]:
            case "impulsive":
                return "buy"
            case "demanding":
                if slot_rent > 50:
                    return "buy"
            case "cautious":
                if player["balance"] - slot_price >= 80:
                    return "buy"
            case "random":
                probability = random.random()
                if probability > 0.5:
                    return "buy"

def player_action(slot, player):

    slot_owner = board[slot]["owner"]
    slot_price = board[slot]["price"]
    slot_rent = board[slot]["rent"]
    
    if slot_owner == '':
        buy_call = buy_decision(slot_price, slot_rent, player)
        
        if buy_call == "buy": # mudar para booleano
            board[slot]["owner"] = player["behavior"]
            player["balance"] -= slot_price
    
    else:
        player["balance"] -= slot_rent
        seu_barriga = list(players.keys())[list(players.values()).index(slot_owner)] # ???
        players[seu_barriga]["balance"] += slot_rent

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

sort_players()

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
