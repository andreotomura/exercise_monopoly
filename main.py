import random
# import pprint 
    # use later

# game = whole match
# turn = every player made their move
# move = the player's move
# action = the player's action

# ---------- PLAYER'S BEHAVIORS ----------

def buy_call(players, player, price, rent):

    result = False

    match players[player]:
       
        case "impulsive": 
            result = True

        case "demanding":
            if rent > 50:
                result = True

        case "cautious":
            if players[player]["balance"] - price >= 80:
                result = True

        case "random":
            probability = random.random()
            if probability >= 0.5:
                result = True

    return result
    
# ---------- SETUP ----------


def generate_board(slots=20):    

    board = []

    for _ in range(slots):
        
        owner = None
        price = random.randrange(150, 450, 50)
        rent = 0.5 /100 * price
        
        slot = {"owner": owner, "price": price, "rent": rent}
        board.append(slot)
    
    return board


def create_players():
    
    players = {
        
        "impulsive": {
            "position": 0,
            "balance": 300,
        },
       
        "demanding": {
            "position": 0,
            "balance": 300,
        },
       
        "cautious": {
            "position": 0,
            "balance": 300,
        },
       
        "random": {
            "position": 0,
            "balance": 300,
        },
    }

    return players


def sort_players(players):
    ''' DEFINE THE ORDER OF PLAYERS IN A TURN '''
    
    list_of_randoms = []
    player_order = []
    good_list = False

    while good_list is False:

        for player in players:
            players[player]["order"] = random.random()
            list_of_randoms.append(players[player]["order"])

        if len(list_of_randoms) == len(set(list_of_randoms)):
            good_list = True

    list_of_randoms.sort(reverse=True)

    for score in list_of_randoms:

        for player in players:

            if players[player]["order"] == score:
                player_order.append(player)    

    return player_order

# ---------- PLAYER FUNCTIONS ----------


def play_action(players, player, board, slot):
    ''' WHAT A PLAYER DOES WHEN IT LANDS ON A SLOT'''

    slot_owner = board[slot]["owner"]
    slot_price = board[slot]["price"]
    slot_rent = board[slot]["rent"]  

    if slot_owner == None:

        if players[player]["balance"] >= slot_price:
            call = buy_call(players, player, slot_price, slot_rent)

            if call is True:
                board[slot]["owner"] = player
                players[player]["balance"] -= slot_price

    else:

        players[player]["balance"] -= slot_rent
        players[slot_owner]["balance"] += slot_rent


def play_round(players, player, board):
    ''' PLAYER'S WHOLE MOVE '''

    dice_roll = roll_dice()
    landing_slot = players[player]["position"] + dice_roll

    if landing_slot > (len(board)-1):
        landing_slot -= len(board)
        players[player]["position"] = landing_slot
        players[player]["turn"] += 1
        players[player]["balance"] += 100

    else:
        players[player]["position"] = landing_slot 

    play_action(players, player, board, landing_slot)


def play_turn(players, board, player_order):

    for player in player_order:
        play_round(players, player, board)

        if players[player]["balance"] < 0:
            player_order.remove(player)

            for slot in board:
                
                if board[slot]["owner"] == players[player]:
                    board[slot]["owner"] == None
    

# ---------- AUXILIARY FUNCTIONS ----------

def roll_dice():

    dice_roll = random.randrange(1, 7)       
    return dice_roll 


def check_winner(player_order):

    if len(player_order) == 1:
        return True

    else:
        return False


def check_balances(players):

    max_balance = 0
    winner = None

    for player in players:

        if players[player]["balance"] > max_balance:
            max_balance = players[player]["balance"]
            winner = player

    return winner   # missing the tie-break


# ---------- MAIN FUNCTIONS ----------

def play_game(board, i=300, t=1000):

    winners = []
    turns = []
    timeouts = []

    count = {}

    players = create_players()

    for sim in range(i):

        print(f"Simulation nº {sim+1}")
        winner = None
        player_order = sort_players(players)

        # while winner == None:
        for turn in range(t):
            if winner == None:    
                play_turn(players, board, player_order)

                if check_winner(player_order) is True:
                    winner = player_order[0]
                    winners.append(winner)
                    turns.append(turn)
                    timeouts.append(False)
                    # print(f"Match ended on turn {turn}.")
                    # print(f'Winner: {winner}, Balance: {players[winner]["balance"]}')
                    break
        
        if winner == None:
            winner = check_balances(players)
            
            turns.append(turn)
            winners.append(winner)
            timeouts.append(True)



        
            # print("Match ended by timeout")
            # print(f'Winner: {winner}, Balance: {players[winner]["balance"]}')
    
    # print(f"Winners list: {winners}")
    # print(f"Turns list: {turns}")
    # print(f"Timeouts list{timeouts}")
    
    # return ?
    
board = generate_board(20)
play_game(board)